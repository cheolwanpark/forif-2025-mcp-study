KAKAO_API_KEY = "" # 본인의 카카오 API 키를 입력하세요.

import requests
from dataclasses import dataclass
from requests_html import AsyncHTMLSession
import asyncio
from asyncio import Semaphore as Sem

@dataclass
class Location:
    lat: float
    lon: float
    name: str

def get_location(query: str) -> Location | None:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": query,
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }
    r = requests.get(url, params=params, headers={"User-Agent": "my-app"})
    data = r.json()
    if data:
        return Location(
            lat=data[0]["lat"],
            lon=data[0]["lon"],
            name=data[0]["name"]
        )
    return None

@dataclass
class Place:
    name: str = ""
    category: str = ""
    phone: str = ""
    url: str = ""

def search_place(keyword: str, loc: Location, radius: int = 2000) -> list[Place] | None:
    headers = {
        "Authorization": f"KakaoAK {KAKAO_API_KEY}"
    }
    response = requests.get(
        "https://dapi.kakao.com/v2/local/search/keyword.json", 
        headers=headers, 
        params={
        "query": keyword,
        "x": loc.lon,
        "y": loc.lat,
        "radius": radius,
    })

    if response.status_code != 200:
        return None
    response = response.json()
    
    places = []
    if response.get("documents"):
        for doc in response["documents"]:
            places.append(Place(
                name=doc["place_name"],
                category=doc["category_name"],
                phone=doc["phone"],
                url=doc["place_url"]
            ))
    return places

@dataclass
class PlaceDetails:
    rating: str = ""
    status: str = ""
    review_count: int = 0

RATING_XPATH = '//*[@id="mainContent"]/div[1]/div[1]/div[2]/div[1]/a/span/span[2]'
STATUS_XPATH = '//*[@id="mainContent"]/div[1]/div[1]/div[3]/div/span[2]'
REVIEW_COUNT_XPATH = '//*[@id="mainContent"]/div[1]/div[1]/div[2]/div[2]/a/span[2]'

async def fetch_place_details(url: str, session: AsyncHTMLSession, sem: Sem) -> PlaceDetails | None:
    async with sem: # 무시해도 돼요 (동시 요청 수 제한)
        res = await session.get(url)

        if res.status_code != 200:
            return None
        
        await res.html.arender(sleep=0.5, timeout=5)

        rating = res.html.xpath(RATING_XPATH, first=True)
        status = res.html.xpath(STATUS_XPATH, first=True)
        review_count = res.html.xpath(REVIEW_COUNT_XPATH, first=True)

        rating = rating.text.strip() if rating else "N/A"
        status = status.text.strip() if status else "N/A"
        review_count = "".join(filter(str.isdigit, review_count.text)) if review_count else "N/A"

        return PlaceDetails(
            rating=rating,
            status=status,
            review_count=int(review_count) if review_count and review_count.isdigit() else -1
        )
    

@dataclass
class PlaceWithDetails:
    name: str = ""
    category: str = ""
    phone: str = ""
    rating: str = ""
    status: str = ""
    review_count: int = 0

async def search_place_with_details(keyword: str, loc: Location, radius: int = 2000) -> list[PlaceWithDetails] | None:
    places = list(search_place(keyword, loc, radius))
    if not places:
        return []
    
    session = AsyncHTMLSession()
    sem = Sem(5) # 무시해도 돼요 (동시 요청 수 제한)
    details = await asyncio.gather(
        *(fetch_place_details(p.url, session, sem) for p in places)
    )
    results = [
        PlaceWithDetails(
            name=p.name, 
            category=p.category, 
            phone=p.phone, 
            rating=d.rating, 
            status=d.status, 
            review_count=d.review_count
        ) for p, d in zip(places, details) if d is not None
    ]
    # 원래는 아래 코드
    # results = []
    # for place in places:
    #     detail = await fetch_place_details(place.url)
    #     if detail:
    #         results.append(PlaceWithDetails(
    #             name=place.name,
    #             category=place.category,
    #             phone=place.phone,
    #             rating=detail.rating,
    #             status=detail.status,
    #             review_count=detail.review_count
    #         ))
    return results
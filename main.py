from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn

app = FastAPI(title="İlan Dedektifi API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_sample_listings(city: str, district: str, category: str):
    return [
        {
            "id": "1",
            "title": f"{city} {district} 2+1 Cadde Üzeri Güvenlikli Rezidans",
            "price": 20475,
            "location": f"{city} / {district}",
            "platform": "Sahibinden",
            "imageUrl": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&auto=format&fit=crop&q=80",
            "originalUrl": "https://www.sahibinden.com",
            "m2": 110,
            "trustScore": 92,
            "sellerType": "Yetkili Gayrimenkul Ofisi",
            "accountAge": "6 Yıllık Kurumsal Mağaza",
            "activeListings": "18 Aktif İlan",
            "firstPublishDate": "3 Gün Önce",
            "isEDevletVerified": True,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Orijinal Fotoğraflar Doğrulandı",
            "priceHistory": [
                {"date": "10 Gün Önce", "price": 23000},
                {"date": "4 Gün Önce", "price": 21500},
                {"date": "Bugün", "price": 20475}
            ]
        },
        {
            "id": "2",
            "title": f"{city} {district} 3+1 Site İçi Kapalı Otoparklı Ferah Daire",
            "price": 24500,
            "location": f"{city} / {district}",
            "platform": "Hepsiemlak",
            "imageUrl": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&auto=format&fit=crop&q=80",
            "originalUrl": "https://www.hepsiemlak.com",
            "m2": 135,
            "trustScore": 88,
            "sellerType": "Doğrulanmış Bireysel Satıcı",
            "accountAge": "3 Yıllık Üye",
            "activeListings": "1 Aktif İlan",
            "firstPublishDate": "1 Hafta Önce",
            "isEDevletVerified": True,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Kopya Görsel Bulunmadı",
            "priceHistory": [
                {"date": "15 Gün Önce", "price": 26000},
                {"date": "Bugün", "price": 24500}
            ]
        },
        {
            "id": "3",
            "title": f"{city} {district} 1+1 Merkezi Konumda Eşyalı Stüdyo",
            "price": 14000,
            "location": f"{city} / {district}",
            "platform": "Emlakjet",
            "imageUrl": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&auto=format&fit=crop&q=80",
            "originalUrl": "https://www.emlakjet.com",
            "m2": 55,
            "trustScore": 79,
            "sellerType": "Gayrimenkul Danışmanı",
            "accountAge": "1 Yıllık Üye",
            "activeListings": "7 Aktif İlan",
            "firstPublishDate": "Dün",
            "isEDevletVerified": False,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Orijinal Çekim",
            "priceHistory": [
                {"date": "Dün", "price": 14000},
                {"date": "Bugün", "price": 14000}
            ]
        }
    ]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "İlan Dedektifi API Canlı"}

@app.get("/listings")
@app.get("/api/listings")
def search_listings(
    city: str = Query(default="Sakarya"),
    district: str = Query(default="Merkez"),
    category: str = Query(default="kiralik"),
    max_budget: Optional[int] = Query(default=None)
):
    items = get_sample_listings(city, district, category)
    if max_budget is not None and max_budget > 0:
        items = [i for i in items if i["price"] <= max_budget]
    return {
        "count": len(items),
        "city": city,
        "district": district,
        "category": category,
        "listings": items
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
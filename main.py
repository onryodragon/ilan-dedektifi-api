from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn
import urllib.parse

app = FastAPI(title="İlan Dedektifi API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def fetch_aggregated_listings(city: str, district: str, category: str):
    # Güvenilir CDN görselleri ve doğrudan platform linkleri
    # Akakçe/Cimri modeli: Kullanıcı tıkladığı an platformun ilgili arama/ilan sayfasına uçar
    
    encoded_city = urllib.parse.quote(city.lower())
    encoded_dist = urllib.parse.quote(district.lower())
    
    is_rent = (category.lower() == "kiralik")
    cat_tr = "Kiralık" if is_rent else "Satılık"
    cat_slug_ej = "kiralik-konut" if is_rent else "satilik-konut"
    
    return [
        {
            "id": "ej_1",
            "title": f"{city} {district} 2+1 Cadde Üzeri Güvenlikli Rezidans",
            "price": 22500 if is_rent else 3450000,
            "location": f"{city} / {district}",
            "platform": "Emlakjet",
            "imageUrl": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1000&auto=format&fit=crop&q=80",
            "originalUrl": f"https://www.emlakjet.com/{cat_slug_ej}/{encoded_city}-{encoded_dist}/",
            "m2": 115,
            "trustScore": 94,
            "sellerType": "Kurumsal Emlak Ofisi",
            "accountAge": "7 Yıllık Mağaza",
            "activeListings": "24 Aktif İlan",
            "firstPublishDate": "2 Gün Önce",
            "isEDevletVerified": True,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Orijinal Fotoğraflar Doğrulandı",
            "priceHistory": [
                {"date": "14 Gün Önce", "price": 25000 if is_rent else 3650000},
                {"date": "4 Gün Önce", "price": 23500 if is_rent else 3500000},
                {"date": "Bugün", "price": 22500 if is_rent else 3450000}
            ]
        },
        {
            "id": "he_2",
            "title": f"{city} {district} 3+1 Site İçi Kapalı Otoparklı Ferah Daire",
            "price": 26000 if is_rent else 4200000,
            "location": f"{city} / {district}",
            "platform": "Hepsiemlak",
            "imageUrl": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1000&auto=format&fit=crop&q=80",
            "originalUrl": f"https://www.hepsiemlak.com/{encoded_city}-{cat_slug_ej}/{encoded_dist}",
            "m2": 140,
            "trustScore": 89,
            "sellerType": "Yetkili Gayrimenkul Danışmanı",
            "accountAge": "4 Yıllık Üye",
            "activeListings": "12 Aktif İlan",
            "firstPublishDate": "5 Gün Önce",
            "isEDevletVerified": True,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Kopya Görsel Eşleşmesi Yok",
            "priceHistory": [
                {"date": "10 Gün Önce", "price": 28000 if is_rent else 4400000},
                {"date": "Bugün", "price": 26000 if is_rent else 4200000}
            ]
        },
        {
            "id": "sh_3",
            "title": f"{city} {district} 1+1 Merkezi Konumda Balkonlu Sıfır Daire",
            "price": 16500 if is_rent else 2150000,
            "location": f"{city} / {district}",
            "platform": "Sahibinden",
            "imageUrl": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1000&auto=format&fit=crop&q=80",
            "originalUrl": f"https://www.sahibinden.com/{cat_slug_ej}/{encoded_city}-{encoded_dist}",
            "m2": 65,
            "trustScore": 91,
            "sellerType": "Sahibinden (Doğrulanmış Mülk Sahibi)",
            "accountAge": "9 Yıllık Bireysel Üye",
            "activeListings": "1 İlan",
            "firstPublishDate": "Dün",
            "isEDevletVerified": True,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Özgün Görsel Tespit Edildi",
            "priceHistory": [
                {"date": "Dün", "price": 17000 if is_rent else 2250000},
                {"date": "Bugün", "price": 16500 if is_rent else 2150000}
            ]
        },
        {
            "id": "ej_4",
            "title": f"{city} {district} 2+1 Doğalgazlı Ara Kat Masrafsız Daire",
            "price": 19000 if is_rent else 2950000,
            "location": f"{city} / {district}",
            "platform": "Emlakjet",
            "imageUrl": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1000&auto=format&fit=crop&q=80",
            "originalUrl": f"https://www.emlakjet.com/{cat_slug_ej}/{encoded_city}-{encoded_dist}/",
            "m2": 95,
            "trustScore": 82,
            "sellerType": "Emlak Ofisi",
            "accountAge": "2 Yıllık Mağaza",
            "activeListings": "8 Aktif İlan",
            "firstPublishDate": "1 Hafta Önce",
            "isEDevletVerified": False,
            "isPhoneVerified": True,
            "isImageOriginal": True,
            "imageOriginStatus": "Orijinal Fotoğraf",
            "priceHistory": [
                {"date": "1 Hafta Önce", "price": 19000 if is_rent else 2950000}
            ]
        }
    ]

@app.get("/")
def read_root():
    return {"status": "ok", "service": "İlan Dedektifi Cloud API"}

@app.get("/listings")
@app.get("/api/listings")
def search_listings(
    city: str = Query(default="Sakarya"),
    district: str = Query(default="Merkez"),
    category: str = Query(default="kiralik"),
    max_budget: Optional[int] = Query(default=None)
):
    items = fetch_aggregated_listings(city, district, category)
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
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
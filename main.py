from fastapi import FastAPI, APIRouter, HTTPException, status

app = FastAPI()
rooter = APIRouter()

products = [
    {"id": 1, "designation": "Ordinateur", "prix": 2300},
    {"id": 2, "designation": "PC", "prix": 200},
    {"id": 3, "designation": "Souris", "prix": 20},
]


@app.get("/")
def index():
    return {"message": "salut"}


@rooter.get("/articles")
def get_all_articles():
    return {"articles": products}


@rooter.post("/articles/add", status_code=status.HTTP_201_CREATED)
def add_product(article: dict):
    products.append(article)
    return {"message": "product added", "entity": article}


@rooter.get("/articles/{article_id}")
def get_article(article_id: int):
    article = next((item for item in products if item["id"] == article_id), None)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"article": article}


@rooter.put("/articles/update/{article_id}")
def update_article(article_id: int, updated_article: dict):
    for index, item in enumerate(products):
        if item["id"] == article_id:
            products[index] = updated_article
            return {"message": "product updated", "entity": updated_article}
    raise HTTPException(status_code=404, detail="Article not found")


app.include_router(rooter)

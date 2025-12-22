from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {"title": "Getting Started", "content": "This is a simple test post created for API development."},
    2: {"title": "FastAPI Basics", "content": "FastAPI allows you to build APIs quickly and with minimal boilerplate."},
    3: {"title": "Dependency Injection", "content": "Dependencies help you keep your code clean and testable."},
    4: {"title": "Async Endpoints", "content": "Async endpoints improve performance when working with I/O operations."},
    5: {"title": "Request Validation", "content": "Pydantic models validate incoming data automatically."},
    6: {"title": "Error Handling", "content": "Proper error handling makes APIs more predictable for clients."},
    7: {"title": "Authentication", "content": "Authentication ensures that only authorized users can access resources."},
    8: {"title": "Authorization", "content": "Authorization defines what an authenticated user is allowed to do."},
    9: {"title": "Testing APIs", "content": "Automated tests help prevent regressions and improve confidence."},
    10: {"title": "Production Readiness", "content": "Logging and monitoring are essential before deploying to production."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")   

    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
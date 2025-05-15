from pymongo import MongoClient
from datetime import datetime

def insert_data():
    # MongoDB에 연결
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용

    # 기존 데이터 삭제 (중복 방지, 선택 사항)
    db.books.drop()
    db.movies.drop()
    db.user_actions.drop()

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002, "genre": "fantasy"},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987, "genre": "realism"},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009, "genre": "fantasy"}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-08T07:00:00Z"}
    ]
    db.user_actions.insert_many(user_actions)

    print("책, 영화, 사용자 행동 데이터 삽입 완료")
    return db, client

def find_books_by_genre(db, genre):
    books_collection = db.books
    query = {"genre": genre}
    projection = {"_id": 0, "title": 1, "author": 1}
    books = books_collection.find(query, projection)
    for book in books:
        print(book)

def calculate_average_ratings(db):
    movies_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]
    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

def find_recent_actions_by_user(db, user_id, limit=5):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id}
    sort_criteria = [("timestamp", -1)]
    actions = user_actions_collection.find(query).sort(sort_criteria).limit(limit)
    for action in actions:
        print(action)

def count_books_by_year(db):
    books_collection = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)

def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
    update = {"$set": {"action": new_action}}
    result = user_actions_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.") 

if __name__ == "__main__":
    # 데이터 삽입 및 db, client 가져오기
    db, client = insert_data()

    # 판타지 장르 책 조회
    print("\n판타지 장르 책 목록:")
    find_books_by_genre(db, "fantasy")

    # 감독별 평균 평점 계산
    print("\n감독별 평균 평점:")
    calculate_average_ratings(db)

    # 사용자 1의 최근 행동 조회
    print("\n사용자 1의 최근 행동 (최대 5개):")
    find_recent_actions_by_user(db, 1)

    # 연도별 책 수 계산
    print("\n연도별 책 수:")
    count_books_by_year(db)

    # 사용자 1의 2023-04-10 이전 'view' 행동을 'seen'으로 업데이트
    print("\n사용자 행동 업데이트:")
    update_user_actions_before_date(db, 1, datetime(2023, 4, 10), "view", "seen")

    # 작업 완료 후 연결 종료
    client.close()
import json
from typing import Optional
from app.core.redis_client import redis_client


class CacheService:
    @staticmethod
    def get(key: str) -> Optional[any]:
        """캐시에서 값 가져오기"""
        try:
            value = redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            print(f"Cache get error: {e}")
            return None
    
    @staticmethod
    def set(key: str, value: any, expire: int = 3600) -> bool:
        """캐시에 값 저장하기"""
        try:
            redis_client.setex(
                key,
                expire,
                json.dumps(value, ensure_ascii=False)
            )
            return True
        except Exception as e:
            print(f"Cache set error: {e}")
            return False
    
    @staticmethod
    def delete(key: str) -> bool:
        """캐시에서 값 삭제하기"""
        try:
            redis_client.delete(key)
            return True
        except Exception as e:
            print(f"Cache delete error: {e}")
            return False
    
    @staticmethod
    def exists(key: str) -> bool:
        """캐시에 키가 존재하는지 확인"""
        try:
            return redis_client.exists(key) > 0
        except Exception as e:
            print(f"Cache exists error: {e}")
            return False

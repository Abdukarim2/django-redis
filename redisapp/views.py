import requests
from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = requests.get("https://jsonplaceholder.typicode.com/posts")
        context = {
            "posts": posts.json()
        }
        return render(request,'home.html', context) 


class DetailView(View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get("id")
        cache_item = cache.get(f"posts:{post_id}")
        if cache_item:
            detail = cache_item
            detail['from'] = "data from redis cache"
        else:
            detail = post_item = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
            detail['from'] = f"""
                                data from jsonplaceholder <br> refresh this page <br> or <br> click this link
                                 <a href="http://localhost:8000/detail/{post_id}">to redis cache</a>
                                """
            cache.set(f"posts:{post_id}", detail)
        context = {
            "post":detail
        }
        return render(request, "detail.html", context)
        

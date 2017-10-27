import os
import facebookinsights as fi

# alternatively, pass an existing page token
from facebookinsights.graph import Post

page = fi.authenticate(token="EAAZADnByYxCYBAB6Pa8STXJzuYWbQZCtP9u7TQ4dkZBJQQv9HFYi4J9fSOfGovWjasSlOB4eXSJqWzZAQSVkOuIWDJrHwj7ZAQGUzZCQWx2zbEjYKNZCwghIdnN9Ab5CC24Qd7m0huc1YJogwHUYCzxglS1s7YCy0Q6GwNwNKbBLwZDZD")

# return a range of page posts
# latest = page.posts.latest(10).get()
# today = page.posts.range(days=1).get()
# quarter = page.posts.range(months=3).get()

print(page.raw)

post = page.posts.range(since="2017-10-26").get()
print(post)

# <Post: 176871714093_10155279525394094 (2017-10-27)>

x = page.insights.daily(['page_posts_impressions']).range(months=1).get()

real_post = post[3] # type: Post
print(real_post.description)

total_likes = post[3].insights.daily(['post_reactions_like_total']).range(months=1).get()
total_love = post[3].insights.daily(['post_reactions_love_total']).range(months=1).get()

total_love = page.insights.daily(['page_actions_post_reactions_like_total']).range(months=1).get()


print(x)
print(total_likes)
print(total_love)

from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),  # Add a pattern for the root URL
  path('upload/', views.upload_data, name='upload_data'),
  path('pricing/', views.pricing, name='pricing'),
  path('blog/', views.blog, name='blog'),  # Blog listing
]

# This registers the upload_data view function with the URL pattern upload/.
# We also give it a name upload_data for future reference.
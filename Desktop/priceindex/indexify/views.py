from django.shortcuts import render, redirect
from .models import Farmer, Crop, PriceRecord
import pandas as pd

def upload_data(request):
  if request.method == 'POST':
    # Handle file upload
    excel_file = request.FILES['price_data']
    
    # Read data from Excel using pandas
    df = pd.read_excel(excel_file)
    
    # Process data (optional)
    # You can manipulate data from the DataFrame (df) before saving
    #  e.g., handle missing values, data cleaning
    
    # Save data to database
    for index, row in df.iterrows():
      farmer, created = Farmer.objects.get_or_create(
          farm_code=row['Farm Code'],
          first_name=row['First Name'],
          last_name=row['Last Name'],
          district=row['District'],
          county=row['County'],
          sub_county=row['Sub-county'],
          parish=row['Parish'],
          contact=row['Contact'],
      )
      crop, created = Crop.objects.get_or_create(name=row['Crop'])
      price_record = PriceRecord.objects.create(
          date=row['Date'],
          price=row['Price'],
          location=row['Location'],
          farmer=farmer,
          crop=crop,
      )
    
    return redirect('index')  # Redirect to a success page (optional)
  else:
    # Display upload form
    return render(request, 'upload_form.html')
  
def index(request):
  return render(request, 'index.html')

def blog(request):
  # Fetch latest blog posts from database (replace with your model/logic)
  posts = []  # Placeholder for list of blog posts

  context = {'posts': posts}
  return render(request, 'blog.html', context)

def pricing(request):
  # Define pricing plans (replace with your data structure)
  plans = [
      {'name': 'Basic', 'price': 9, 'features': ['Track 3 Crops', 'Limited Price History']},
      {'name': 'Pro', 'price': 29, 'features': ['Unlimited Crops', 'Advanced Analytics']},
      {'name': 'Enterprise', 'price': 49, 'features': ['Customizable Reports', 'Dedicated Support']},
  ]

  context = {'pricing': plans}
  return render(request, 'pricing.html', context)

#Explanation: 
# This code addresses the previous error by using the `Crop` model instead of the removed `Product` model.
# The data upload process now saves crop information to the `Crop` model, linking it to the corresponding `PriceRecord`.

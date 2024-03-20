from django.db import models

class Farmer(models.Model):
  farm_code = models.CharField(max_length=20, unique=True)  # Unique identifier for the farm (required)
  first_name = models.CharField(max_length=50, blank=False)  # Farmer's first name (required)
  last_name = models.CharField(max_length=50)
  district = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  sub_county = models.CharField(max_length=50)
  parish = models.CharField(max_length=50)
  contact = models.CharField(max_length=20)  # Phone number or email
  crop = models.CharField(max_length=50, default="Unknown")  # Name of the crop or livestock
  acreage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

  def __str__(self):
    return f"{self.farm_code} - {self.first_name} {self.last_name}"


class Crop(models.Model):
  name = models.CharField(max_length=50)  # Name of the crop or livestock

  def __str__(self):
    return self.name


class FarmerCrop(models.Model):
  farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)  # Link to Farmer model
  crop = models.ForeignKey(Crop, on_delete=models.CASCADE)  # Link to Crop model
  acreage = models.DecimalField(max_digits=10, decimal_places=2)  # Acreage for this specific crop-farmer combination

  class Meta:
    unique_together = (('farmer', 'crop'),)  # Enforce unique combination of farmer and crop

  def __str__(self):
    return f"{self.farmer} - {self.crop} ({self.acreage} acres)"


class PriceRecord(models.Model):
  date = models.DateField()
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price with decimals
  location = models.CharField(max_length=20, choices=[('Domestic', 'Domestic'), ('International', 'International')])
  farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)  # Link to Farmer model
  # Removed foreign key to Product
  crop = models.ForeignKey(Crop, on_delete=models.CASCADE)  # Link to Crop model (replaced Product)

  def __str__(self):
    return f"{self.crop} - {self.date} ({self.location}) - {self.farmer}"

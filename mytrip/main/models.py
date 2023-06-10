from django.db import models

# Create your models here.

# schema 정의
class barrier_free_hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    FCLTY_NM = models.CharField(max_length=100)
    RDNMADR_NM = models.CharField(max_length=100)
    CTPRVN_CD = models.IntegerField()
    SIGNGU_CD = models.IntegerField()
    FCLTY_LO = models.FloatField()
    FCLTY_LA = models.FloatField()
    AREA_NM = models.CharField(max_length=100)
    HMPG_URL = models.CharField(max_length=100)
    HOTEL_GRAD_NO = models.CharField(max_length=100)
    TEL_NO = models.CharField(max_length=100)
    GSRM_CO = models.FloatField()
    GSRM_AR_VALUE = models.CharField(max_length=100)
    GSRM_SVC_POSBL_AT = models.CharField(max_length=100)
    DSPSN_FCLTY_AT = models.CharField(max_length=100)
    BASE_DE = models.CharField(max_length=100)

class categorized(models.Model):
    field1 = models.IntegerField()
    title = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    contentid = models.IntegerField()
    contenttypeid = models.IntegerField()
    firstimage = models.CharField(max_length=100)
    firstimage2 = models.CharField(max_length=100)
    mapx = models.FloatField()
    mapy = models.FloatField()
    tel = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
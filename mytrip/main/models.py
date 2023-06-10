from django.db import models

# Create your models here.

# schema 정의
class barrier_free_hotel(models.Model):
    id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return self.FCLTY_NM

class categorized(models.Model):
    id = models.AutoField(primary_key=True)
    field1 = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100, null=True)
    addr2 = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    contentid = models.IntegerField(null=True)
    contenttypeid = models.IntegerField(null=True)
    firstimage = models.CharField(max_length=100, null=True)
    firstimage2 = models.CharField(max_length=100, null=True)
    mapx = models.FloatField(null=True)
    mapy = models.FloatField(null=True)
    tel = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

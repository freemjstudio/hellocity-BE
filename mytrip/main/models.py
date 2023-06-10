from django.db import models

# Create your models here.

# schema 정의
class barrier_free_hotel(models.Model):
    id = models.AutoField(primary_key=True)
    FCLTY_NM = models.CharField(max_length=100, null=True)
    RDNMADR_NM = models.CharField(max_length=100, null=True)
    CTPRVN_CD = models.IntegerField(null=True)
    SIGNGU_CD = models.IntegerField(null=True)
    FCLTY_LO = models.FloatField(null=True)
    FCLTY_LA = models.FloatField(null=True)
    AREA_NM = models.CharField(max_length=100, null=True)
    HMPG_URL = models.CharField(max_length=100, null=True)
    HOTEL_GRAD_NO = models.CharField(max_length=100, null=True)
    TEL_NO = models.CharField(max_length=100, null=True)
    GSRM_CO = models.FloatField(null=True)
    GSRM_AR_VALUE = models.CharField(max_length=100, null=True)
    GSRM_SVC_POSBL_AT = models.CharField(max_length=100, null=True)
    DSPSN_FCLTY_AT = models.CharField(max_length=100, null=True)
    BASE_DE = models.CharField(max_length=100, null=True)

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

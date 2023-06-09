from django.db import models

# Create your models here.

# schema 정의
class barrier_free_hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    FCLTY_NM = models.CharField()
    RDNMADR_NM = models.CharField()
    CTPRVN_CD = models.IntegerField()
    SIGNGU_CD = models.IntegerField()
    FCLTY_LO = models.FloatField()
    FCLTY_LA = models.FloatField()
    AREA_NM = models.CharField()
    HMPG_URL = models.CharField()
    HOTEL_GRAD_NO = models.CharField()
    TEL_NO = models.CharField()
    GSRM_CO = models.FloatField()
    GSRM_AR_VALUE = models.CharField()
    GSRM_SVC_POSBL_AT = models.CharField()
    DSPSN_FCLTY_AT = models.CharField()
    BASE_DE = models.CharField()
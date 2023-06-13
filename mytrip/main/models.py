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
    parking = models.CharField(max_length=500, null=True)
    route = models.CharField(max_length=500, null=True)
    publictransport = models.CharField(max_length=500, null=True)
    ticketoffice = models.CharField(max_length=500, null=True)
    promotion = models.CharField(max_length=500, null=True)
    wheelchair = models.CharField(max_length=500, null=True)
    exit = models.CharField(max_length=500, null=True)
    elevator = models.CharField(max_length=500, null=True)
    restroom = models.CharField(max_length=500, null=True)
    auditorium = models.CharField(max_length=500, null=True)
    room = models.CharField(max_length=500, null=True)
    handicapetc = models.CharField(max_length=500, null=True)
    braileblock = models.CharField(max_length=500, null=True)
    helpdog = models.CharField(max_length=500, null=True)
    guidehuman = models.CharField(max_length=500, null=True)
    audioguide = models.CharField(max_length=500, null=True)
    bigprint = models.CharField(max_length=500, null=True)
    brailepromotion = models.CharField(max_length=500, null=True)
    guidesystem = models.CharField(max_length=500, null=True)
    blindhandicapetc = models.CharField(max_length=500, null=True)
    singuide = models.CharField(max_length=500, null=True)
    videoguide = models.CharField(max_length=500, null=True)
    hearingroom = models.CharField(max_length=500, null=True)
    hearinghandicapetc = models.CharField(max_length=500, null=True)
    stroller = models.CharField(max_length=500, null=True)
    lactationroom = models.CharField(max_length=500, null=True)
    babysparechair = models.CharField(max_length=500, null=True)
    infantsfamilyetc = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

class transportation(models.Model):
    contentid = models.IntegerField(null=True)
    parking = models.CharField(max_length=500, null=True)
    route = models.CharField(max_length=500, null=True)
    publictransport = models.CharField(max_length=500, null=True)
    ticketoffice = models.CharField(max_length=500, null=True)
    promotion = models.CharField(max_length=500, null=True)
    wheelchair = models.CharField(max_length=500, null=True)
    exit = models.CharField(max_length=500, null=True)
    elevator = models.CharField(max_length=500, null=True)
    restroom = models.CharField(max_length=500, null=True)
    auditorium = models.CharField(max_length=500, null=True)
    room = models.CharField(max_length=500, null=True)
    handicapetc = models.CharField(max_length=500, null=True)
    braileblock = models.CharField(max_length=500, null=True)
    helpdog = models.CharField(max_length=500, null=True)
    guidehuman = models.CharField(max_length=500, null=True)
    audioguide = models.CharField(max_length=500, null=True)
    bigprint = models.CharField(max_length=500, null=True)
    brailepromotion = models.CharField(max_length=500, null=True)
    guidesystem = models.CharField(max_length=500, null=True)
    blindhandicapetc = models.CharField(max_length=500, null=True)
    singuide = models.CharField(max_length=500, null=True)
    videoguide = models.CharField(max_length=500, null=True)
    hearingroom = models.CharField(max_length=500, null=True)
    hearinghandicapetc = models.CharField(max_length=500, null=True)
    stroller = models.CharField(max_length=500, null=True)
    lactationroom = models.CharField(max_length=500, null=True)
    babysparechair = models.CharField(max_length=500, null=True)
    infantsfamilyetc = models.CharField(max_length=500, null=True)

# 교통약자 지하철 역 편의 시설
class station_info(models.Model):
    course1 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=100)
    station = models.CharField(max_length=100)
    no = models.IntegerField
    telno_info = models.CharField()
    station_image = models.CharField()
    exit_info = models.CharField(null=True)
    line
    icon_path
    elevater
    elevater_txt
    time_info2
    time_info3
    line_name
    time_info1
    station_image2
    time_info4
    useyn

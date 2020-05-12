from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('claim_procedure',views.claim_link,name='claimprocedure'),
    path('claim_home',views.claim_home,name="claim_home"),
    path('renew_procedure',views.renew_link,name="renewprocedure"),
    path('insure_procedure',views.insure_link,name="insureprocedure")
    
   
    


]
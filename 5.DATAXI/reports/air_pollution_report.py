import streamlit as st
import pandas as pd


def kpi_brooklyn(carros):
    
    volume_brooklyn = 58420 * 4 * 24
    pm_brooklyn = 9.26
    pm_brooklyn=pm_brooklyn*0.05
   
    new_volume_brooklyn = (volume_brooklyn-(carros*4*24))
    new_pm_brooklyn= (new_volume_brooklyn*pm_brooklyn)/volume_brooklyn
    ptc_disminuye = (new_pm_brooklyn - pm_brooklyn)/pm_brooklyn
    brooklyn=round(-100*ptc_disminuye,2)
    
    return brooklyn

    
def kpi_manhattan(carros):
    
    volume_manhattan = 49682 * 4 * 24
    pm_manhattan = 11
    pm_manhattan=pm_manhattan*0.05
   
    new_volume_manhattan = (volume_manhattan-(carros*4*24))
    new_pm_manhattan= (new_volume_manhattan*pm_manhattan)/volume_manhattan
    ptc_disminuye = (new_pm_manhattan - pm_manhattan)/pm_manhattan
    manhattan=round(-100*ptc_disminuye,2)
    
    return manhattan
    

def kpi_queen(carros):
    volume_queen = 54046 * 4 * 24
    pm_queen = 9
    pm_queen=pm_queen*0.05
   
    new_volume_queen = (volume_queen-(carros*4*24))
    new_pm_queen= (new_volume_queen*pm_queen)/volume_queen
    ptc_disminuye = (new_pm_queen - pm_queen)/pm_queen
    queen=round(-100*ptc_disminuye,2)
    
       
    return queen

def kpi_staten_island(carros):
    volume_staten_island = 8962 * 4 * 24
    pm_staten_island = 8.5
    pm_staten_island=pm_staten_island*0.05
   
    new_volume_staten_island = (volume_staten_island-(carros*4*24))
    new_pm_staten_island= (new_volume_staten_island*pm_staten_island)/volume_staten_island
    ptc_disminuye = (new_pm_staten_island - pm_staten_island)/pm_staten_island
    staten_island=round(-100*ptc_disminuye,2)
    
    return staten_island

def kpi_the_bronx(carros):
    
    volume_the_bronx = 31839 * 4 * 24
    pm_the_bronx = 9.7
    pm_the_bronx=pm_the_bronx*0.05
   
    new_volume_bronx = (volume_the_bronx-(carros*4*24))
    new_pm_the_bronx= (new_volume_bronx*pm_the_bronx)/volume_the_bronx
    ptc_disminuye = (new_pm_the_bronx - pm_the_bronx)/pm_the_bronx
    the_bronx=round(-100*ptc_disminuye,2)
    
    return the_bronx

def taxis(carros):
    
    volume_taxi = 7737
    pm_nyc = 0.47
  
   
    new_volume_taxi = (volume_taxi-carros)
    new_pm_nyc= (new_volume_taxi*pm_nyc)/volume_taxi
    ptc_disminuye = (new_pm_nyc - pm_nyc)/pm_nyc
    taxis=round(-100*ptc_disminuye,2)
    return taxis
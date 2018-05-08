#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:09:02 2018

@author: valentinarodriguez
"""



def dataCleaning(data, columnsToDrop):
    data = data.drop(columnsToDrop, axis=1)
    data = data.fillna(0)
    print("dataCleaning")
    print(data)
    return data


def convertingCrimeCategoryNumericalToClass(data):
     #violent crimes from 1 to 4
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=1,value= 1)
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=2,value= 1)
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=3,value= 1)
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=4,value= 1)
      #violent crimes from 5 to 7
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=5,value=-1)
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=6,value=-1)
     data["Statute_CrimeCategory"] = data["Statute_CrimeCategory"].replace(to_replace=7,value=-1)
     return data


def convertingCategorizedDataToNumerical(data):
    data = convertingCrimeCategoryNumericalToClass(data)
    data = convertingWeaponDescriptionFeatureToNumerical(data)
    data = convertingLarcenyTypeFeatureToNumerical(data)
    data = convertingLocationTypeFeatureToNumerical(data)
    data = convertingSeasonFeatureToNumerical(data)
    print("convertingCategorizedDataToNumerical")
    print(data)
    return data
    

def convertingWeaponDescriptionFeatureToNumerical(data):
    data= data.replace(to_replace="* No Weapon Specified *",value=0)
    data= data.replace(to_replace="Unknown",value=0)
    data= data.replace(to_replace="None/Not Applicable",value=0)
    data= data.replace(to_replace="Not Reported",value=0)
    data= data.replace(to_replace="Other Weapon",value=0)
    data= data.replace(to_replace="Blunt Object",value=1)
    data= data.replace(to_replace="Fire/Incendiary Device",value=2)
    data= data.replace(to_replace="Firearm",value=3)
    data= data.replace(to_replace="Fully Automatic Handgun or Submachine Gun",value=4)
    data= data.replace(to_replace="Imitation Firearm",value=5)
    data= data.replace(to_replace="Knife/Cutting Instrument",value=6)
    data= data.replace(to_replace="Motor Vehicle",value=7)
    data= data.replace(to_replace="Shotgun",value=8)
    data= data.replace(to_replace="Simulated Firearm",value=9)
    data= data.replace(to_replace="Personal Weapons",value=10)
    data= data.replace(to_replace="Physical Force",value=11)
    data= data.replace(to_replace="Revolver, Derringer, or Single-shot Pistol",value=12)
    data= data.replace(to_replace="Semiautomatic Handgun",value=13)
    data= data.replace(to_replace="Drug/Narcotics/Sleeping Pills",value=14)
    data= data.replace(to_replace="Explosives",value=15)
    data= data.replace(to_replace="Fully Automatic Rifle or Machine Gun",value=16)
    data= data.replace(to_replace="Poison",value=17)
    data= data.replace(to_replace="Semiautomatic Rifle",value=18)
    data= data.replace(to_replace="Single Shot, Pump Action, or Bolt Action Rifle",value=19)
    return data





def convertingLarcenyTypeFeatureToNumerical(data):
    data= data.replace(to_replace="* No Larceny Type Specified *",value=0)
    data= data.replace(to_replace="All Other Larcenies",value=1)
    data= data.replace(to_replace="Motor Vehicle Theft",value=2)
    data= data.replace(to_replace="Pocket-picking",value=3)
    data= data.replace(to_replace="Purse-snatching",value=4)
    data= data.replace(to_replace="Shoplifting",value=5)
    data= data.replace(to_replace="Theft from Building",value=6)
    data= data.replace(to_replace="Theft from Coin-Operated Machine or Device",value=7)
    data= data.replace(to_replace="Theft from Mailbox",value=8)
    data= data.replace(to_replace="Theft from Motor Vehicle",value=9)
    data= data.replace(to_replace="Theft of Motor Vehicle Parts or Accessories",value=10)
    data= data.replace(to_replace="Not Applicable",value=0)
    data= data.replace(to_replace="Not Reported",value=0)
    data= data.replace(to_replace="Unknown",value=0)
    return data




def convertingLocationTypeFeatureToNumerical(data):
    data= data.replace(to_replace="* No Location Scene Specified *",value=0)
    data= data.replace(to_replace="***",value=0)
    data= data.replace(to_replace="Amusement Center",value=1)
    data= data.replace(to_replace="Auto Sales Lot",value=2)
    data= data.replace(to_replace="Auto Shop",value=3)
    data= data.replace(to_replace="Bar",value=4)
    data= data.replace(to_replace="Barber/Beauty Shop",value=5)
    data= data.replace(to_replace="Buy/Sell/Trade Shop",value=6)
    data= data.replace(to_replace="Cemetery",value=7)
    data= data.replace(to_replace="Church",value=8)
    data= data.replace(to_replace="Clothing Store",value=9)
    data= data.replace(to_replace="College",value=10)
    data= data.replace(to_replace="Department/Discount Store",value=11)
    data= data.replace(to_replace="Construction Site",value=12)
    data= data.replace(to_replace="Doctor's Office",value=13)
    data= data.replace(to_replace="Drug Store",value=14)
    data= data.replace(to_replace="Dry Cleaners/Laundry",value=15)
    data= data.replace(to_replace="Factory/Mill/Plant",value=16)
    data= data.replace(to_replace="Field/Woods",value=17)
    data= data.replace(to_replace="Financial Institution",value=18)
    data= data.replace(to_replace="Garage/Shed",value=19)
    data= data.replace(to_replace="Gas Station",value=20)
    data= data.replace(to_replace="Government Office",value=21)
    data= data.replace(to_replace="Grocery/Supermarket",value=22)
    data= data.replace(to_replace="Hospital",value=23)
    data= data.replace(to_replace="Hotel/Motel",value=24)
    data= data.replace(to_replace="Jail/Prison",value=25)
    data= data.replace(to_replace="Jewelry Store",value=26)
    data= data.replace(to_replace="Lake/Waterway",value=27)
    data= data.replace(to_replace="Liquor Store",value=28)
    data= data.replace(to_replace="Multiple Dwelling",value=29)
    data= data.replace(to_replace="Not Reported",value=0)
    data= data.replace(to_replace="Other Business Office",value=30)
    data= data.replace(to_replace="Other Commercial Service Location",value=31)
    data= data.replace(to_replace="Other Outside Location",value=32)
    data= data.replace(to_replace="Other Public Access Building",value=33)
    data= data.replace(to_replace="Other Residential",value=34)
    data= data.replace(to_replace="Other Retail Store",value=35)
    data= data.replace(to_replace="Park/Playground",value=36)
    data= data.replace(to_replace="Parking Garage",value=37)
    data= data.replace(to_replace="Parking Lot",value=38)
    data= data.replace(to_replace="Professional Office",value=39)
    data= data.replace(to_replace="Public Transit Vehicle",value=40)
    data= data.replace(to_replace="Rental Storage Facility",value=41)
    data= data.replace(to_replace="Residential Facility",value=42)
    data= data.replace(to_replace="Restaurant",value=43)
    data= data.replace(to_replace="School",value=44)
    data= data.replace(to_replace="Shopping Mall",value=45)
    data= data.replace(to_replace="Single Family Home",value=46)
    data= data.replace(to_replace="Sporting Goods",value=47)
    data= data.replace(to_replace="Street",value=48)
    data= data.replace(to_replace="Transit Facility",value=49)
    data= data.replace(to_replace="Unknown",value=0)
    data= data.replace(to_replace="Variety/Convenience Store",value=50)
    data= data.replace(to_replace="Yard",value=51)
    data= data.replace(to_replace="Other Building",value=52)
    return data


def convertingSeasonFeatureToNumerical(data):
    data= data.replace(to_replace="Spring",value=1)
    data= data.replace(to_replace="Autumn",value=2)
    data= data.replace(to_replace="Winter",value=3)
    data= data.replace(to_replace="Summer",value=4)
    return data


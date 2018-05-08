
/*
UPDATE THE SEASON INFORMATION IN RPD__Part_I_Crime_2011_to_Present TABLE BASED ON THE OccurredFrom_Date
OBTAINED FROM http://www.glib.com/season_dates.html
EACH YEAR WILL HAVE A DIFFERENT START/END SEASON DATE (YYYY-MM-DD).
FOLLOWING THE DATE_FORMAT https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html
*/
ALTER TABLE RPD__Part_I_Crime_2011_to_Present ADD Season VARCHAR(20);


#BEGIN test datetime-----
SELECT OccurredFrom_Timestamp, DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') 
FROM RPD__Part_I_Crime_2011_to_Present 
where OBJECTID = 10

SELECT MAX(DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i')), MIN(DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i'))
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2011' and  DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') > DATE_FORMAT('2011-12-22 00:30', '%Y-%m-%d %H:%i');

SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2011' and  DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') > DATE_FORMAT('2011-12-22 00:30', '%Y-%m-%d %H:%i');

SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2011'

#RESULT:13353
#END TEST-----

#------------------------------ YEAR 2011- 13353 rows affected ------------------------------ 
#winter - 336 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2011' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') > DATE_FORMAT('2011-12-22 00:30', '%Y-%m-%d %H:%i');
commit;
#winter - 2141 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2011' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') < DATE_FORMAT('2011-03-20 19:20', '%Y-%m-%d %H:%i');
commit;

#spring 3261 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2011' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2011-03-20 19:21', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2011-06-21 13:15', '%Y-%m-%d %H:%i');
commit;
#summer 3988 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2011' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2011-06-21 13:16', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2011-09-23 05:03', '%Y-%m-%d %H:%i');
commit;
#autumn 3627 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2011' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2011-09-23 05:04', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2011-12-22 00:29', '%Y-%m-%d %H:%i');
commit;

#------------------------------ YEAR 2012 - 12619 rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2012'
#result: 12619

#winter -  291 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2012' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') > DATE_FORMAT('2012-12-21 06:11', '%Y-%m-%d %H:%i');
commit;
#winter -  2206 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2012' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') < DATE_FORMAT('2012-03-20 01:13', '%Y-%m-%d %H:%i');
commit;

#spring  3306 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2012' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2012-3-20 01:14', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2012-06-20 19:08', '%Y-%m-%d %H:%i');
commit;
#summer  3746 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2012' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2012-06-20 19:09', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2012-09-22 10:48', '%Y-%m-%d %H:%i');
commit;
#autumn 3070 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2012' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2012-09-22 10:49', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2012-12-21 06:10', '%Y-%m-%d %H:%i');
commit;


#------------------------------ YEAR 2013 - 11851 rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2013'
#result: 11851

#winter -  248 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2013' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') >= DATE_FORMAT('2013-12-21 12:11', '%Y-%m-%d %H:%i');
commit;
#winter -  2033 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2013' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2013-03-20 07:01', '%Y-%m-%d %H:%i');
commit;

#spring  3147 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2013' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2013-3-20 07:02', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2013-06-21 01:03', '%Y-%m-%d %H:%i');
commit;
#summer 3510  rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2013' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2013-06-21 01:04', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2013-09-22 16:43', '%Y-%m-%d %H:%i');
commit;
#autumn  2913 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2013' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2013-09-22 16:44', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2013-12-21 12:10', '%Y-%m-%d %H:%i');
commit;


#------------------------------ YEAR 2014 -  10332 rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2014'
#result: 10332

#winter - 239  rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2014' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') >= DATE_FORMAT('2014-12-21 18:03', '%Y-%m-%d %H:%i');
commit;
#winter -  1649 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2014' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2014-03-20 12:56', '%Y-%m-%d %H:%i');
commit;

#spring  2499 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2014' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2014-03-20 12:57', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2014-06-21 06:50', '%Y-%m-%d %H:%i');
commit;
#summer  3425 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2014' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2014-06-21 06:51', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2014-09-22 22:28', '%Y-%m-%d %H:%i');
commit;
#autumn  2520 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2014' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2014-09-22 22:29', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2014-12-21 18:02', '%Y-%m-%d %H:%i');
commit;

#------------------------------ YEAR 2015 - 9859  rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2015'
#result: 9859

#winter -  241 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2015' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') >= DATE_FORMAT('2015-12-21 23:48', '%Y-%m-%d %H:%i');
commit;
#winter -  1482 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2015' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2015-03-20 18:44', '%Y-%m-%d %H:%i');
commit;

#spring  2503 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2015' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2015-03-20 18:45', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2015-06-21 12:37', '%Y-%m-%d %H:%i');
commit;
#summer  3063 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2015' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2015-06-21 12:38', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2015-09-23 04:19', '%Y-%m-%d %H:%i');
commit;
#autumn  2570 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2015' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2015-09-23 04:20', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2015-12-21 23:47', '%Y-%m-%d %H:%i');
commit;

#------------------------------ YEAR 2016 - 9350  rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2016'
#result: 9350

#winter -  250 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2016' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') >= DATE_FORMAT('2016-12-21 05:44', '%Y-%m-%d %H:%i');
commit;
#winter -  1719 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2016' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2016-03-20 00:29', '%Y-%m-%d %H:%i');
commit;

#spring  2280 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2016' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2016-03-20 00:30', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2016-06-20 18:33', '%Y-%m-%d %H:%i');
commit;
#summer  2645 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2016' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2016-06-20 18:34', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2016-09-22 10:20', '%Y-%m-%d %H:%i');
commit;
#autumn  2456 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2016' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2016-09-22 10:21', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2016-12-21 05:43', '%Y-%m-%d %H:%i');
commit;

#------------------------------ YEAR 2017 -  9550 rows affected ------------------------------ 
# (YYYY-MM-DD).
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2017'
#result: 9550

#winter - 192  rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2017' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') >= DATE_FORMAT('2017-12-21 11:28', '%Y-%m-%d %H:%i');
commit;
#winter - 1804  rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2017' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2017-03-20 06:27', '%Y-%m-%d %H:%i');
commit;

#spring  2386 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Spring'
WHERE OccurredFrom_Date_Year='2017' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2017-03-20 06:28', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2017-06-21 00:23', '%Y-%m-%d %H:%i');
commit;
#summer 2900  rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Summer'
WHERE OccurredFrom_Date_Year='2017' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2017-06-21 00:24', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2017-09-22 16:01', '%Y-%m-%d %H:%i');
commit;
#autumn  2268 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Autumn'
WHERE OccurredFrom_Date_Year='2017' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') BETWEEN DATE_FORMAT('2017-09-22 16:02', '%Y-%m-%d %H:%i') AND DATE_FORMAT('2017-12-21 11:27', '%Y-%m-%d %H:%i');
commit;

#----test-----

SELECT MAX(DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i')), MIN(DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i'))
FROM RPD__Part_I_Crime_2011_to_Present 

#------------------------------ YEAR 2018 - 1143  rows affected ------------------------------ 
# (YYYY-MM-DD). UNTIL MARCH 6TH
#test
SELECT count(*) as quantity
FROM RPD__Part_I_Crime_2011_to_Present 
WHERE OccurredFrom_Date_Year='2018'
#result: 1143

#winter -  1143 rows affected
UPDATE RPD__Part_I_Crime_2011_to_Present 
set Season = 'Winter'
WHERE OccurredFrom_Date_Year='2018' and 
DATE_FORMAT(OccurredFrom_Timestamp,'%Y-%m-%d %H:%i') <= DATE_FORMAT('2018-03-20 12:14', '%Y-%m-%d %H:%i');
commit;
#----test---
SELECT *
FROM RPD__Part_I_Crime_2011_to_Present WHERE season= NULL


SELECT *
FROM RPD__Part_I_Crime_2011_to_Present WHERE (season !='Winter' and season !='Spring' and season !='Summer' and season !='Autumn')
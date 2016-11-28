select uid, concat(snid,"-",level) as "range", count(2)
  from quests
 where date BETWEEN STR_TO_DATE('2016-02-08', '%Y-%m-%d')
                and STR_TO_DATE('2016-02-14', '%Y-%m-%d')
   and status = "COMPLETED"
   GROUP BY uid, "range";
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import csv


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobSatellite.settings')
    django.setup()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
#@@@@@@@@@@@@@@@@@@@@@@@@@@
from recommend.models import jobdict, recruit_info,company,skill

CSV_PATH=r'C:\Users\네리\Desktop\sba_re\4조\job_dict_final.csv'

with open(CSV_PATH,newline='',encoding="utf-8")as csvfile:
    data_reader=csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        jobdict.objects.create(job=row['job'],skill=row['skill'])

CSV_PATH2=r'C:\Users\네리\Desktop\sba_re\4조\total_skill_data29.csv'

with open(CSV_PATH2,newline='',encoding="utf-8")as csvfile:
    data_reader=csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        recruit_info.objects.create(titleId=row['jobId'],company=row['company'],
                                    title=row['title'],job=row['job'],skill=row['skill'],
                                    region=row['region'],task=row['task'],require=row['require'],
                                    prefer=row['prefer'],jobUrl=row['jobUrl'],total_skill=row['total_skill'],
                                    total_skill_literal=row['total_skill_literal'])

CSV_PATH3=r'C:\Users\네리\Desktop\sba_re\4조\company_rating_list_new.csv'

with open(CSV_PATH3,newline='',encoding="utf-8")as csvfile:
    data_reader=csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        company.objects.create(companyId=row['companyId'],company_name=row['company'],reviewCount=row['reviewCount'],
                               average=row['average'],salary=row['salary'],wlb=row['wlb'],culture=row['culture'],
                               possibility=row['possibility'],management=row['management'])

CSV_PATH4=r'C:\Users\네리\Desktop\sba_re\4조\skillPerJob.csv'

with open(CSV_PATH4,newline='',encoding="utf-8")as csvfile:
    data_reader=csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        skill.objects.create(needSkill=row['index'],web=row['웹개발'],network=row['네트워크/보안/운영'],se=row['시스템엔지니어'],
                             soft=row['소프트웨어엔지니어'],qa=row['QA(Quality Assurance)'],plan=row['기획'],
                             da=row['데이터분석'],app=row['모바일앱개발'],pm=row['프로젝트매니저'],
                             game=row['게임개발'],dba=row['DBA(Database Admin.)'],consulting=row['컨설팅'],
                             he=row['하드웨어엔지니어'],cd=row['캐릭터디자인'],
                             gd=row['그래픽디자인'],ad=row['애니메이션디자인'],marketing=row['마케팅'],
                             market=row['시장조사/분석'],sa=row['소프트웨어아키텍트'],wp=row['웹퍼블리셔'],
                             ud=row['UI/UX/GUI디자인'],md=row['상품개발/기획/MD'],strategy=row['경영기획/전략'],
                             advertise=row['광고/시각디자인'],video=row['영상/모션디자인'],sales=row['영업기획/관리/지원'],
                             support=row['경영지원'],erp=row['ERP'],iu=row['일러스트레이터'],
                             wd=row['웹디자인'],machine=row['기계'],esemi=row['전자/반도체'],
                             control=row['제어'],elec=row['전기'],dsemi=row['반도체/디스플레이'],
                             econtrol=row['전기/전자/제어'],domsales=row['국내영업'],
                             sound=row['음악/음향/사운드'],itsol=row['IT/솔루션영업'],emarketing=row['온라인마케팅'],
                             smarketing=row['전략마케팅'],bd=row['브랜드디자인'],bmarketing=row['브랜드마케팅'],
                             publish=row['출판/편집디자인'],pd=row['방송연출/PD/감독'],cs=row['고객지원/CS'],
                             culture=row['조직문화'],
                             crm=row['CRM'],maintenance=row['유지/수리/정비'],tech=row['기술영업'],product=row['제품/산업디자인'])

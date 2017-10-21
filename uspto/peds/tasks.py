# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@ip-tools.org>
import celery
from uspto.peds.client import UsptoPatentExaminationDataSystemClient
from uspto.util.tasks import GenericDownloadTask

class UsptoPatentExaminationDataSystemDownloadTask(GenericDownloadTask):
    name = 'uspto.peds.tasks.UsptoPatentExaminationDataSystemDownloadTask'
    client_factory = UsptoPatentExaminationDataSystemClient
    pass

@celery.shared_task(bind=True, base=UsptoPatentExaminationDataSystemDownloadTask)
def download_task(self, query):
    """
    https://celery.readthedocs.io/en/latest/userguide/tasks.html#basics
    http://docs.celeryproject.org/en/latest/whatsnew-4.0.html#the-task-base-class-no-longer-automatically-register-tasks
    """
    return self.process(query)

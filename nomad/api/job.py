import requests

class Job(object):
    ENDPOINT = "job"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)


    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):

        try:
            j = self._get(item)
            return True
        except requests.RequestException:
            return False
        except BaseException:
            return False

    def __getitem__(self, item):

        try:
            j = self._get(item)

            if j["ID"] == item:
                return j
            if j["Name"] == item:
                return j
            else:
                raise KeyError
        except requests.RequestException:
            raise KeyError
        except BaseException:
            return KeyError


    def _get(self,*args):
        url = self._requester._endpointBuilder(Job.ENDPOINT,*args)
        job = self._requester.get(url)

        return job.json()

    def get_job(self,id):
        return self._get(id)

    def get_allocations(self,id):
        return self._get(id,"allocations")

    def get_evaluations(self,id):
        return self._get(id,"evaluations")

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Job.ENDPOINT,*args)

        if kwargs:
            response = self._requester.post(url,json=kwargs["job"])
        else:
            response = self._requester.post(url)

        return response.json()

    def register_job(self,id,job):
        return self._post(id,job=job)

    def evaluate_job(self,id):
        return self._post(id,"evaluate")

    def periodic_job(self,id):
        return self._post(id,"periodic","force")


















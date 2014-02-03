class Setter(object):
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

class FakeRequest(Setter):
    pass

class FakeResponse(Setter):
    pass

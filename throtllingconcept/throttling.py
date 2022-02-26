from rest_framework.throttling import UserRateThrottle

class RamRateThrottle(UserRateThrottle):
    scope = 'raj'
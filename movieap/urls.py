# from rest_framework.routers import SimpleRouter
# from .views import MovieOperations
#
#
# simpleRouter=SimpleRouter()
#
# simpleRouter.register('movie',MovieOperations)
#
# urlpatterns=simpleRouter.urls

from rest_framework.routers import SimpleRouter
# from .views import BookOperations
from .views import MovieOperations

simpleRouter = SimpleRouter()

# simpleRouter.register('book',BookOperations)

simpleRouter.register('movie',MovieOperations)

urlpatterns = simpleRouter.urls
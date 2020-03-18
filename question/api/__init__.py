from hybridrouter import HybridRouter

from .level import LevelViewSet

QuestionHybridRouter = HybridRouter()
QuestionHybridRouter.register('level', LevelViewSet)



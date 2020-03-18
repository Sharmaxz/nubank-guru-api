from hybridrouter import HybridRouter

from .level import LevelViewSet
from .question import QuestionViewSet

QuestionHybridRouter = HybridRouter()
QuestionHybridRouter.register('level', LevelViewSet)
QuestionHybridRouter.register('question', QuestionViewSet)



from .manager import provider_registry
from .gemini import GeminiProvider
from .groq import GroqProvider
from .fallback import RobustFallbackProvider

# Initialize providers
gemini_provider = GeminiProvider()
groq_provider = GroqProvider()

# Setup robust fallback: Try Groq first for blazing speed, fallback to Gemini if rate limited
fallback_provider = RobustFallbackProvider(providers=[groq_provider, gemini_provider])

# Register providers
provider_registry.register(gemini_provider)
provider_registry.register(groq_provider)

# Set the fallback chain as the default AI engine for all tasks
provider_registry.register(fallback_provider, set_as_default=True)

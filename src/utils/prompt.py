from jinja2 import Template

from src.enums.llm import RoleEnum


# This class is the same as src.bot.utils.text
# But i thought that here I can break "DRY" for better structure

class Prompt:
    def __init__(self, text: str):
        self.text = text

    def render(self, **kwargs) -> str:
        return Template(self.text).render(**kwargs)
    
    
class LLMPrompt:
    def __init__(
        self,
        prompt: str,
        role: RoleEnum):
        self.prompt = prompt
        self.role = role
    
    @property
    def message(self) -> dict:
        return {
            "role": self.role,
            "content": self.prompt
        }
    
class SystemPrompt(LLMPrompt):
    def __init__(self, prompt: str):
        super().__init__(prompt, RoleEnum.system.value)
        
        
class UserPrompt(LLMPrompt):
    def __init__(self, prompt: str):
        super().__init__(prompt, RoleEnum.user.value)
        
        
class AIPrompt(LLMPrompt):
    def __init__(self, prompt: str):
        super().__init__(prompt, RoleEnum.ai.value)

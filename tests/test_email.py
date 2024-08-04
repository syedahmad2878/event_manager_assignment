from unittest.mock import AsyncMock
import pytest
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager
import settings

    
@pytest.fixture
def email_service():
    if settings.send_real_mail == 'true':
        return EmailService()
    else:
        mock_service = AsyncMock(spec=EmailService)
        mock_service.send_verification_email.return_value = None
        mock_service.send_user_email.return_value = None
        return mock_service

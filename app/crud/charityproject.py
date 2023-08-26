from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        project = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        return project.scalars().first()
    

    async def get_projects_by_completion_rate(self, session: AsyncSession):
        """Возвращает список закрытых проектов отсортированных по скорости сбора средств."""
        stmt = (
            select(
                CharityProject,
                (
                    func.strftime("%s", CharityProject.close_date).__sub__(
                        func.strftime("%s", CharityProject.create_date)
                    )
                ).label("completion_rate"),
            )
            .where(CharityProject.fully_invested.is_(True))
            .order_by("completion_rate")
        )
        closed_projects = await session.execute(stmt)
        return closed_projects


charity_project_crud = CRUDCharityProject(CharityProject)

from db.db import db_session
from fastapi import Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.processing.process import Process


class SearchService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def search(self, query):
        # Instantiate processing class
        process = Process(query)
        # Call main method
        response = await process.main()
        # Save query to history
        # Return results
        return response

from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeSection(BaseModel):
    name: str
    latexCode: str


class PreTitleSection(ResumeSection):
    '''
    PreTitleSection contains latex code related to imports, styling and custom commands
    '''


class HeadingSection(ResumeSection):
    '''
    HeadingSection contains name and personal information like phone no, email and socials
    '''    

class SkiilsSection(ResumeSection):
    '''
    SkiilsSection contains user technicall skills
    '''
    
class ExperienceSection(ResumeSection):
    '''
    ExperienceSection contains work experience such as jobs and internships
    '''

class ProjectsSection(ResumeSection):
    '''
    ProjectsSection contains users projects, synced from github repos and other sources 
    '''

class EducationSection(ResumeSection):
    '''
    EducationSection contains educational qualificaions
    '''
class AdditionalSection(ResumeSection):
    '''
    AdditionalSection contains information like certificates, awards and publications
    '''

class Resume(BaseModel):
    sectionNames: list[str]
    sections: list[ResumeSection]

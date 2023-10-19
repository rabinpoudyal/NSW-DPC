from __future__ import annotations
import dataclasses
from dataclasses import dataclass, field


import logging
from typing import Any, Dict, List, Optional, Tuple, Union

logger = logging.getLogger(__name__)

@dataclass
class PatentSchema:
    '''
    Class to represent a patent schema.
    '''

    # Patent metadata
    patent_id: str
    patent_title: str
    patent_abstract: str
    patent_date: str
    patent_year: str
    patent_type: str
    patent_kind: str
    patent_num_claims: int
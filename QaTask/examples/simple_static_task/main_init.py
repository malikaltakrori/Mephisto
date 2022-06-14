#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from mephisto.abstractions.blueprints.static_html_task.static_html_blueprint import (
    BLUEPRINT_TYPE_STATIC_HTML,
)

from dataclasses import dataclass, field

from mephisto.tools.scripts import task_script
from mephisto.operations.hydra_config import build_default_task_config

from omegaconf import DictConfig, MISSING

from mephisto.abstractions.blueprints.abstract.static_task.static_blueprint import (
    SharedStaticTaskState,
)
from mephisto.data_model.qualification import QUAL_EXISTS
from mephisto.utils.qualifications import make_qualification_dict


# https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html#MasterQualifications


# @dataclass
# class MyTaskConfig(build_default_task_config('example')):
#     server_source_path: str = field(
#         default=MISSING,
#         metadata={
#             "help": (
#                 "Optional path to a prepared server directory containing everything "
#                 "needed to run a server of the given type. Overrides server type. "
#             )
#         },
#     )

@task_script(default_config_file="local")
def main(operator, cfg: DictConfig) -> None:
    shared_state = SharedStaticTaskState()

    # only in the main task, i.e. after doing this one.
    # shared_state.qualifications = [
    # make_qualification_dict(
    #     "maliks_Qual",
    #     QUAL_EXISTS, None
    # ),
    # ]
    
    # shared_state.mturk_specific_qualifications = [
    #     {
    #         "QualificationTypeId": "2F1QJWKUDD8XADTFD2Q0G6UTO95ALH",  #<-- AMT
    #         # "QualificationTypeId": "2ARFPLSP75KLA8M8DH1HTEQVJT3SY6",  # <-- sandbox
    #         "Comparator": "Exists",
    #     },
    # ]

    operator.launch_task_run(cfg.mephisto, shared_state)
    operator.wait_for_runs_then_shutdown(skip_input=True, log_rate=30)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from mephisto.abstractions.blueprints.static_html_task.static_html_blueprint import (
    BLUEPRINT_TYPE_STATIC_HTML,
)
from mephisto.tools.scripts import task_script
from omegaconf import DictConfig


@task_script(default_config_file="local")
def main(operator, cfg: DictConfig) -> None:
    
    # ... when launching a task
    # shared_state.qualifications = [
    #     make_qualification_dict(
    #         ALLOWLIST_QUALIFICATION,
    #         QUAL_EXISTS,
    #     ),
    #     make_qualification_dict(
    #         BLOCKLIST_QUALIFICATION,
    #         QUAL_NOT_EXISTS,
    #     ),
    # ]
    
    
    operator.launch_task_run(cfg.mephisto)
    operator.wait_for_runs_then_shutdown(skip_input=True, log_rate=30)


if __name__ == "__main__":
    main()

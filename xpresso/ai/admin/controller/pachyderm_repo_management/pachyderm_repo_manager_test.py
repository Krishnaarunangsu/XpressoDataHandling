from xpresso.ai.core.logging.xpr_log import XprLogger
from xpresso.ai.admin.controller.exceptions.xpr_exceptions import *
from xpresso.ai.admin.controller.pachyderm_repo_management.pachyderm_client \
    import PachydermClient
from xpresso.ai.core.utils.xpr_config_parser import XprConfigParser




class PachydermRepoManager:
    """
    Manages repos on pachyderm cluster
    """
    def __init__(self, config_path=XprConfigParser.DEFAULT_CONFIG_PATH):
        #self.logger = XprLogger()
        #self.config = XprConfigParser(config_path)["pachyderm"]
        self.pachyderm_client = self.connect_to_pachyderm()

    def connect_to_pachyderm(self):
        """
        connects to pachyderm cluster and returns a PfsClient connection instance

        :return:
            returns a PfsClient Object
        """
        client = PachydermClient(
            "172.16.3.51","30650"
        )
        return client


if __name__ == "__main__":
    p = PachydermRepoManager()
    print(p)


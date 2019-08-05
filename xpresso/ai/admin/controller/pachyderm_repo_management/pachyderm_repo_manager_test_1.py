# from xpresso.ai.core.logging.xpr_log import XprLogger
# from xpresso.ai.admin.controller.exceptions.xpr_exceptions import *
import python_pachyderm  as pachyderm
from xpresso.ai.admin.controller.pachyderm_repo_management.pachyderm_client \
    import PachydermClient
from xpresso.ai.core.utils.xpr_config_parser import XprConfigParser




class PachydermRepoManager:
    """
    Manages repos on pachyderm cluster
    """
    def __init__(self, list_of_repo: list):
        #self.logger = XprLogger()
        #self.config = XprConfigParser(config_path)["pachyderm"]
        self.list_of_repo = list_of_repo
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
        # client.create_new_repo('test_repo2')

        self.list_of_repo=client.get_repo()
        print(self.list_of_repo)


        return client

    # def creating_first_repo(self):
    #
    #     client.create_repo('test_Anushree')
    #     with client.commit('test_Anushree', 'master') as c:
    #      client.put_file_bytes(c, '/dir_a/data.txt', b'DATA')
    #     client.get_repo()
    #     return

        # with client.commit('test', 'master') as c:
        #     client.put_file_bytes(c, '/dir_a/data.txt', b'DATA')




if __name__ == "__main__":
    p = PachydermRepoManager(list_of_repo=list())

    print(p)




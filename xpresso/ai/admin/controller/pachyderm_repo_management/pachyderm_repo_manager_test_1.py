# from xpresso.ai.core.logging.xpr_log import XprLogger
# from xpresso.ai.admin.controller.exceptions.xpr_exceptions import *
import python_pachyderm  as pachyderm
from xpresso.ai.admin.controller.pachyderm_repo_management.pachyderm_client \
    import PachydermClient
from xpresso.ai.core.utils.xpr_config_parser import XprConfigParser
import re
import json


class PachydermRepoManagerTest:
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
        print(f'Client:{client}')
        #client.create_new_repo('test_abzooba_dvc_5')
        self.new_repo = client.create_new_repo('test_abzooba_dvc_3')
        print(f'Repo Created:\n{self.new_repo}')
        #self.list_of_repo=client.get_repo()
        #print(self.list_of_repo)


        return client


    def create_repo(self, repo_json):
        """
        creates a new repo on pachyderm cluster
        :param repo_json:
            Information of the repo to be created
        :return:
        """
        if "repo_name" not in repo_json:
            #raise RepoNotProvidedException()R
            raise Exception
        if not self.name_validity_check(repo_json["repo_name"]):
            #raise PachydermFieldsNameException()
            raise Exception
        description = ""
        if "description" in repo_json:
            description = repo_json["description"]

        print()
        self.pachyderm_client.create_new_repo(repo_json["repo_name"],
                                              description)
        return


    @staticmethod
    def name_validity_check(name):
        """
        Checks if the name provided contains only alphanumeric characters,
        underscore or dashes

        :param name:
            (str) : name
        :return:
            check status i.e. True or False
        """
        accepted_pattern = r"[\w, -]+$"
        if not isinstance(name, str):
            # raise PachydermFieldsNameException()
            raise Exception
        match = re.match(accepted_pattern, name)
        if not match:
            return False
        return True


    def delete_repo(self, repo_name):
        """
        deletes a repo from pachyderm cluster

        This is admin level operation
        :param repo_name:
            name of the repo to be deleted
        :return:
            no return statement
        """
        self.pachyderm_client.delete_repo(repo_name)

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
    p = PachydermRepoManagerTest(list_of_repo=list())

     # read file
    with open('create_repo.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)# show values
    print("usd: " + str(obj['repo_name']))
    p.create_repo(obj)
    #p.delete_repo('test_repo2')
    #p = PachydermRepoManager()
    #p.connect_to_pachyderm()
    #p.create_repo()



    #print(p)




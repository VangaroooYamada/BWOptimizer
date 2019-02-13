import networkx as nx
import yaml
from addon import Addon
from item import Item
from offering import Offering
from perk import Perk

class BloodWeb():

    def __init__(self):
        self.bw = nx.read_edgelist('testBW.txt', nodetype=int)
        with open('testAttr.yml', 'r') as test:
            tmp = test.read()
        self.attr_dict = yaml.safe_load(tmp)
        for node, attr in self.attr_dict.items():
            self.attr_dict[node] = eval(attr)
        nx.set_node_attributes(self.bw, name='node_type', values=self.attr_dict)
        nx.set_node_attributes(self.bw, name='status', values='unpassed')
        self.bw.nodes[0]['status'] = 'passed'
        self.entity_trigger = False
        self.expend_bp = 0
        self.route = []


    def test_func(self):
        return 
        
# *********************************************************

    def get_shortest(self):
        # unimplemented
        self.entity_trigger = False
        root_list = []
                    
        while self.exists_unpassed():
            
            if self.entity_trigger:
                # do entity's Erosion method
                # self.entity()
                for i in self.bw.nodes[::-1]:
                    if self.bw.nodes[i]['status'] == 'unpassed':
                        self.bw.nodes[i]['status'] == 'entity'

            else:
                for i in self.bw.nodes:
                    if self.bw.nodes[i]['status'] == 'unpassed':
                        if type(self.bw.nodes[i]['node_type']) == Perk:
                            root_list = nx.dijkstra_path(self.bw, 0, i)
                            print(root_list)
                            for n in root_list:
                                self.bw.nodes[n]['status'] = 'passed'
                            self.entity_trigger = True
                            break
                continue                        

    def get_optimal(self):
        # unimplemented
        return

    def get_selected_optimal(self):
        # unimplemented
        return

# *********************************************************

    def entity(self):
        # unimplemented
        # change 'unpassed' nodes' status 'entity'
        return

    def exists_unpassed(self):
        return 'unpassed' in nx.get_node_attributes(self.bw, 'status').values()

    def show_info(self):
        for node, attr in dict(self.bw.nodes).items():
            print('{0} -> {1}'.format(node, attr))
        print('Number of Nodes: {0}'.format(nx.number_of_nodes(self.bw)))
        print('Number of Edges: {0}'.format(nx.number_of_edges(self.bw)))


if __name__ == '__main__':
    test = BloodWeb()
    # test.show_info()
    print('*' * 20)
    test.test_func()
    # test.get_shortest()
    print('*' * 20)
    test.show_info()
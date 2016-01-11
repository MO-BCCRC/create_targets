'''
Created on Sep 08, 2014

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    GATK RealignerTargetCreator : Create suspecious regions where a realignment will be done
    '''
    def __init__(self, component_name='create_targets', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        GATK RealignerTargetCreator : Create suspecious regions where a realignment will be done
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        create_targets_jar = self.requirements['gatk']
        create_targets_infile = self.args.infile
        create_targets_outfile = self.args.outfile
        create_targets_ref_genome = self.args.ref_genome

        cmd = self.requirements['java']
        cmd_args = [
                    java_mem,
                    java_jar_option,
                    create_targets_jar,
                    "-T", "RealignerTargetCreator",
                    "-R", create_targets_ref_genome,
                    "-I", create_targets_infile,
                    "-o", create_targets_outfile
                   ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    create_targets = Component()
    create_targets.args = component_ui.args
    create_targets.run()

if __name__ == '__main__':

    import component_ui

    _main()

class Problem_Params:
    def __init__(self):
        self.coupled = 3 # CoupledBioheatFlow
        self.coupled_set(self.coupled)
        self.tissueMeshNumber=2
        self.numberOfElementNodes = 4
        self.number_of_element_nodes_set(self.tissueMeshNumber)
        # time parameters, bioheat
        self.timeIncrementBioheat = 10
        self.startTimeBioheat = 0.0
        self.timeStepsBioheat = 301
        self.diffusionOutputFrequency = 100
        # time parameters, flow
        self.flowOutputFrequency = 1
        self.startTimeFlow = 0.0
        self.timeStepsFlow = 1
        self.timeIncrementFlow = 0.1
        
        self.conductivity_blood   = 0.5
        self.rho_blood            = 1069.0
        self.c_blood              = 3650.0
        self.rho_muscle           = 1085.0   #   muscle density
        self.c_muscle             = 3768.0        # J/Kg.K   muscle specific heat
        self.rho_bone             = 1357.0   # kg/mm3    bone density
        self.c_bone               = 1700.0        # J/Kg.K   bone specific heat
        self.rho_skin             = 1085.0   # kg/mm3    skin density
        self.c_skin               = 3680.0        # J/Kg.K   skin specific heat

        self.k_muscle             = 0.42     # W/mm.K muscle conductivity.
        self.k_bone               = 0.75     # W/mm.K bone conductivity.
        self.k_skin               = 0.47     # W/mm.K skin conductivity.

        self.h_conv             = 2.0      # W/mm2.K
        #h_conv            = 200.0*1e-6    # W/mm2.K for water
        self.hr_rad             = 5.9      # W/mm2.K See example 3.12 Incropera

        # R_arm              = 0.03          # m

        self.Tblood             = 37.0          # C blood temeprature
        self.Tair               = 17.7          # C
        self.Tinit_tissue       = 36.3 
        self.Tinit_skin         = 20.0
        self.Tinit_blood        = 37.0
        self.Tinlet_bl          = 37.0

        self.skin_L             = 3

        self.w_perfusion        = 5e-4          # 1/s terminal blood flow per volume of tissue.

        self.qm_0                    = 700.0           # Basal metabolic heat
        self.Nusselt                 = 4.0   

        self.tissue_input_files_set(self.tissueMeshNumber)



    def coupled_set(self, value):
        self.testFlow           = (value == 1)
        self.bioheat            = (value == 2)
        self.CoupledBioheatFlow = (value == 3)       

    def tissue_input_files_set(self, value):
        if value==1:
            self.numberOfNodesTissue    = 58557
            self.numberOfElementsTissue = 253489
            self.tissueElementsFile = 'input/bioheat/elements2.csv'
            self.tissueNodesFile    = "input/bioheat/nodes.csv"
            self.boundaryNodesFile  =  'input/bioheat/boundary_nodes.csv'
        elif value==2:
            self.numberOfNodesTissue    = 48083
            self.numberOfElementsTissue = 248166
            self.tissueElementsFile = 'input/bioheat/mesh2/elements.csv'
            self.tissueNodesFile    = "input/bioheat/mesh2/nodes.csv"
            self.boundaryNodesFile  = 'input/bioheat/mesh2/boundary_nodes.csv'
        elif value==3:
            self.numberOfNodesTissue    = 225
            self.numberOfElementsTissue = 128
            self.tissueElementsFile = 'input/bioheat/mesh3/elements.csv' 
            self.tissueNodesFile    = "input/bioheat/mesh3/nodes.csv"
            self.boundaryNodesFile  = 'input/bioheat/mesh3/boundary_nodes.csv'   

    def number_of_element_nodes_set(self, value): 
        if value == 3:
            self.numberOfElementNodes = 8
        else:
            self.numberOfElementNodes = 4



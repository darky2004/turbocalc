#!/Users/dark/anaconda/bin/python
from math import sqrt,log

# constants
R = 287.06 # Specific gas constant
Rho = 1.225 # Air density at sea level, kg/m^3
LHV = 4.31E7 # Kerosene lower heating value, J/kg
CRITICAL_NPR = 1.8929 # Chocked Nozzle Mach No

# a single spool turbojet parts list
ENGINE_1 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 100,
        'P_INTAKE': 101325,
        'T_INTAKE': 288,
        'P_LOSS':0.01
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':22,
        'EFF':0.87
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1570,
        'P_LOSS':0.05
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC'],
        'EFF':0.87
    },
    {
        'ID':'NOZZLE',
        'TYPE':'NOZZLE',
        'P_LOSS':0.0
    }
    #{
    #    'ID':REHEAT,
    #    'TYPE':'AFTERBURNER',
    #    'TET': 1500,
    #    'P_LOSS':0.01
    #},
    #{
    #    'ID':'FPT',
    #    'TYPE':'TURBINE',
    #    'W_MATCH':[],
    #    'M_EXIT':0.05,
    #    'EFF':0.92
    #},

]

ENGINE_9HA = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 826,
        'P_INTAKE': 101325,
        'T_INTAKE': 288,
        'P_LOSS':0.01
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':21.8,
        'EFF':0.79
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1690,
        'P_LOSS':0.05
    },
    {
        'ID':'HPT',
        'TYPE':'POWER_TURBINE',
        'W_MATCH':['HPC'],
        'M_EXIT':0.05,
        'EFF':0.82
    },
]

# a single spool turbofan
ENGINE_1A = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 114,
        'P_INTAKE': 101325,
        'T_INTAKE': 288,
        'P_LOSS':0.0
    },
    {
        'ID':'FAN',
        'TYPE':'FAN',
        'BPR':0.9,
        'FPR':3.5,
        'EFF':0.88
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':8,
        'EFF':0.86
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1550,
        'P_LOSS':0.05
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC','FAN'],
        'EFF':0.86
    },
    {
        'ID':'NOZZLE',
        'TYPE':'NOZZLE',
        'P_LOSS':0.0
    }
]

# two-spool turbofan (GE90)
ENGINE_2 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 1100,
        'P_INTAKE': 101325,
        'T_INTAKE': 300,
        'P_LOSS':0.02
    },
    {
        'ID':'FAN',
        'TYPE':'FAN',
        'BPR':9,
        'FPR':1.5,
        'EFF':0.95
    },
    {
        'ID':'LPC',
        'TYPE':'COMPRESSOR',
        'PR':5,
        'EFF':0.88
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':4,
        'EFF':0.88
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1600,
        'P_LOSS':0.01
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC','LPC'],
        'EFF':0.92
    },
    {
        'ID':'LPT',
        'TYPE':'TURBINE',
        'W_MATCH':['FAN'],
        'EFF':0.92
    },
    {
        'ID':'NOZZLE',
        'TYPE':'NOZZLE',
        'P_LOSS':0.01
    }
]

# three-spool turbofan (RB211)
ENGINE_3 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 1200,
        'P_INTAKE': 101325,
        'T_INTAKE': 300,
        'P_LOSS':0.01
    },
    {
        'ID':'FAN',
        'TYPE':'FAN',
        'BPR':10,
        'FPR':1.5,
        'EFF':0.95
    },
    {
        'ID':'IPC',
        'TYPE':'COMPRESSOR',
        'PR':5,
        'EFF':0.88
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':4,
        'EFF':0.88
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1773,
        'P_LOSS':0.01
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC'],
        'EFF':0.92
    },
    {
        'ID':'IPT',
        'TYPE':'TURBINE',
        'W_MATCH':['IPC'],
        'EFF':0.92
    },
    {
        'ID':'LPT',
        'TYPE':'TURBINE',
        'W_MATCH':['FAN'],
        'EFF':0.92
    },
    {
        'ID':'NOZZLE',
        'TYPE':'NOZZLE',
        'P_LOSS':0.01
    }
]

# a turboshaft without FPT
ENGINE_4 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 70.5,
        'P_INTAKE': 101325,
        'T_INTAKE': 300,
        'P_LOSS':0.01
    },
    {
        'ID':'LPC',
        'TYPE':'COMPRESSOR',
        'PR':4,
        'EFF':0.88
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':5,
        'EFF':0.88
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1500,
        'P_LOSS':0.01
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC'],
        'EFF':0.92
    },
    {
        'ID':'LPT',
        'TYPE':'POWER_TURBINE',
        'W_MATCH':['LPC'],
        'M_EXIT':0.05,
        'EFF':0.92
    },
]

# turboshaft with FPT
ENGINE_5 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 70.5,
        'P_INTAKE': 101325,
        'T_INTAKE': 300,
        'P_LOSS':0.01
    },
    {
        'ID':'LPC',
        'TYPE':'COMPRESSOR',
        'PR':4,
        'EFF':0.88
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':5,
        'EFF':0.88
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1500,
        'P_LOSS':0.05
    },
    {
        'ID':'HPT',
        'TYPE':'TURBINE',
        'W_MATCH':['HPC','LPC'],
        'EFF':0.92
    },
    {
        'ID':'FPT',
        'TYPE':'POWER_TURBINE',
        'M_EXIT':0.05,
        'W_MATCH':[],
        'EFF':0.92
    },
]


# land power turbine with intercooler and recuperator
ENGINE_6 = [
    {
        'ID':'INTAKE',
        'TYPE':'INTAKE',
        'MFLOW_TOTAL': 400,
        'P_INTAKE': 101000,
        'T_INTAKE': 288,
        'P_LOSS':0.0
    },
    {
        'ID':'LPC',
        'TYPE':'COMPRESSOR',
        'PR':4,
        'EFF':0.88
    },
    {
        'ID':'INTERCOOLER',
        'TYPE':'INTERCOOLER',
        'EFF':1.0,
        'T_COLD':300,
        'P_LOSS':0.03
    },
    {
        'ID':'HPC',
        'TYPE':'COMPRESSOR',
        'PR':10,
        'EFF':0.88
    },
    {
        'ID':'RECUPERATOR',
        'TYPE':'RECUPERATOR',
        'EFF':0.95,
        'P_LOSS':0.05,
        'INPUT_SOURCE':'HPC',
        'HEAT_SOURCE':'HPT'
    },
    {
        'ID':'COMBUSTOR',
        'TYPE':'COMBUSTOR',
        'TET':1700,
        'P_LOSS':0.05
    },
    {
        'ID':'HPT',
        'TYPE':'POWER_TURBINE',
        'W_MATCH':['HPC','LPC'],
        'M_EXIT':0.05,
        'EFF':0.88
    }
]


CP_VALUES = {
     200 : 1001, 550 : 1040, 1000 : 1142, 1700 : 1229,
     250 : 1003, 600 : 1051, 1100 : 1155, 1800 : 1237,
     300 : 1005, 650 : 1063, 1200 : 1173, 1900 : 1244,
     350 : 1008, 700 : 1075, 1300 : 1190, 2000 : 1250,
     400 : 1013, 750 : 1087, 1400 : 1204, 2100 : 1255,
     450 : 1020, 800 : 1099, 1500 : 1216, 2200 : 1260,
     500 : 1029, 900 : 1121, 1600 : 1221, 2300 : 1265
}

GAMMA_VALUES = {
     200 : 1.402, 550 : 1.381, 1000 : 1.366, 1700 : 1.305,
     250 : 1.401, 600 : 1.376, 1100 : 1.331, 1800 : 1.302,
     300 : 1.400, 650 : 1.370, 1200 : 1.324, 1900 : 1.300,
     350 : 1.398, 700 : 1.364, 1300 : 1.318, 2000 : 1.298,
     400 : 1.395, 750 : 1.359, 1400 : 1.313, 2100 : 1.295,
     450 : 1.391, 800 : 1.354, 1500 : 1.309, 2200 : 1.294,
     500 : 1.387, 900 : 1.344, 1600 : 1.308, 2300 : 1.293
}

def interpolate(t,TABLE):
    if t in TABLE:
        return TABLE[t]
    else:
        lower=int(round(t/100,0)*100)
        upper=int(round(t/100,0)+1)*100
        x = (TABLE[lower]+(t-lower)*(TABLE[upper]-TABLE[lower])/(upper-lower))
        return x

def cp_calc(t):
    return interpolate(t,CP_VALUES)

def gamma_calc(t):
    return interpolate(t,GAMMA_VALUES)

def heat_exchanger(t_in, p_in, t_exit, p_loss, n_is):
    t_out = t_in - n_is*(t_in-t_exit)
    p_out = p_in * (1-p_loss)
    return t_out, p_out

def converging_nozzle_thrust(t,p,p_amb,mflow):
    npr = p/p_amb
    y = gamma_calc(t)
    if npr>CRITICAL_NPR:
        npr = CRITICAL_NPR # Mach No = 1.0
    t_out = t/(npr**((y-1)/y))
    p_out = p/npr
    density = p_out/(R*t_out)
    if npr<CRITICAL_NPR:
        mach_no = sqrt((t/t_out-1)*2/(y-1))
    else:
        mach_no = 1.0
    u = sqrt(y*t_out*R)
    area = mflow/(density*u*mach_no)
    f = mflow*u*mach_no+(p_out-p_amb)*area
    print("\tNozzle area is %3.2f m^2" % area)
    print("\tMach number  is %3.2f m^2" % mach_no)
    return {'AREA_NOZZLE':area,'EXIT_P':p_out,'MACH_NO':mach_no, 'V_EXIT':u,'THRUST':f }

def plot_cycle_charts(t1,t2,t3,t4,p1,p2,p3,p4):
    # plot T-E cycle chart
    deltaS_12 = cp_calc(t1)*log(t2/t1) - R*log(p2/p1);
    deltaS_23 = deltaS_12 + cp_calc(t2)*log(t3/t2) - R*log(p3/p2);
    deltaS_34 = deltaS_23 + cp_calc(t3)*log(t4/t3) - R*log(1/(p3/p4));
    plt.plot([0,deltaS_12, deltaS_23, deltaS_34,0],[t1,t2,t3,t4,t1])
    plt.xlabel('Entropy')
    plt.ylabel('Temperature, K')
    plt.title('T-E Brayton cycle chart')
    plt.grid(True)
    plt.show()

def compressor_stage(T_in, P_in, PR, N_eff):
    y = gamma_calc(T_in)
    T_out_is = T_in*PR**((y-1)/y)
    T = T_in + (T_out_is-T_in)/N_eff
    P = P_in*PR
    return (T,P)

def compute_engine(component_data):
    works = {}
    thrusts = []
    energies = []
    index = 0
    stations = []
    mass_flow = 0.0
    total_flow= 0.0
    fuel_flow = 0.0
    engine_class = "TURBOJET"
    second_pass = False
    P_amb = 0
    T_amb = 0
    W_net = 0.0
    F_net = 0.0
    Q_in = 0.0
    for item in component_data:
        if item['TYPE'] == 'INTAKE':
            T_amb = item['T_INTAKE']
            P_amb = item['P_INTAKE']
            mass_flow = item['MFLOW_TOTAL']
            total_flow = mass_flow
            stations.extend([
                {
                    'ID':'ENTRY',
                    'T':item['T_INTAKE'],
                    'P':item['P_INTAKE']
                },
                {
                    'ID':item['ID'],
                    'T':item['T_INTAKE'],
                    'P':item['P_INTAKE']*(1-item['P_LOSS'])
                }
            ])
            index = index+1
        if item['TYPE'] == 'FAN':
            engine_class = "TURBOFAN"
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            T_out, P_out = compressor_stage(T_in,P_in,item['FPR'],item['EFF'])
            works[item['ID']]=cp_calc(T_in)*(T_out - T_in)*mass_flow
            #split the air flow after fan exit
            mass_flow = mass_flow/(item['BPR']+1)
            fan_flow = mass_flow*item['BPR']
            print('FAN:')
            fan_thrust = converging_nozzle_thrust(T_out,P_out,P_amb,fan_flow)
            thrusts.append(fan_thrust['THRUST'])
            energies.append((fan_flow*fan_thrust['V_EXIT']**2)/2)
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index + 1
        if item['TYPE'] == 'COMPRESSOR':
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            T_out, P_out = compressor_stage(T_in,P_in,item['PR'],item['EFF'])
            works[item['ID']]=cp_calc(T_in)*(T_out - T_in)*mass_flow
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index + 1
        if item['TYPE'] == 'INTERCOOLER':
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            T_out, P_out = heat_exchanger(T_in, P_in, item['T_COLD'], item['P_LOSS'], item['EFF'])
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index + 1
        if item['TYPE'] == 'RECUPERATOR':
            # first pass - pressure loss only
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            p_loss =  item['P_LOSS']
            T_out = T_in
            P_out = P_out*(1-p_loss)
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index + 1
            second_pass = True
        if item['TYPE'] == 'COMBUSTOR':
            P_in = stations[index]['P']
            T_in = stations[index]['T']
            T_out = item['TET']
            Q_in = cp_calc(T_out)*(T_out - T_in)*mass_flow
            fuel_flow = Q_in/LHV
            mass_flow = mass_flow + fuel_flow
            total_flow = total_flow + fuel_flow
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out*(1-item['P_LOSS'])})
            index = index + 1
        if item['TYPE'] == 'TURBINE':
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            cp_turb = cp_calc(T_in)
            y = gamma_calc(T_in)
            # match the turbine to corresponding compressor
            W_t = 0
            for x in item['W_MATCH']:
                W_t = W_t + works[x]
            T_out = T_in - W_t/(cp_turb*mass_flow)
            T_out_is = T_in-(T_in-T_out)/item['EFF']
            P_out = P_in / ((T_in/T_out_is)**(y/(y-1)))

            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index + 1

        if item['TYPE'] == 'POWER_TURBINE':
            engine_class = "TURBOSHAFT"
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            cp_turb = cp_calc(T_in)
            M_exit = item['M_EXIT']
            y = gamma_calc(T_amb)
            P_out = P_amb*(1+(y-1)/2*M_exit**2)**(y/(y-1));
            T_out_is = T_in*(P_in/P_out)**((1-y)/y);
            T_out = T_in - (T_in-T_out_is)*item['EFF'];
            # subtract the residual work from net work
            W_net = (T_in-T_out)*cp_turb*mass_flow;
            for x in item['W_MATCH']:
                W_net = W_net - works[x]
            stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
            index = index +1
        if item['TYPE'] == 'NOZZLE':
            T_in = stations[index]['T']
            P_in = stations[index]['P']
            T_out = T_in
            P_out = P_in*(1-item['P_LOSS'])
            print('CORE:')
            core_thrust = converging_nozzle_thrust(T_out,P_out,P_amb,mass_flow)
            energies.append((mass_flow*core_thrust['V_EXIT']**2)/2)
            thrusts.append(core_thrust['THRUST'])

    # second pass for recuperator calculation
    if second_pass:
        for item in component_data:
            if item['TYPE'] == 'RECUPERATOR':
                n_eff = item['EFF']
                p_loss = item['P_LOSS']
                index = -1
                for x in stations:
                    if x['ID'] == item['INPUT_SOURCE']:
                        index = stations.index(x)
                    if x['ID'] == item['HEAT_SOURCE']:
                        T_source = x['T']
                T_in = stations[index]['T']
                P_in = stations[index]['P']
                T_out, P_out = heat_exchanger(T_in, P_in, T_source, p_loss, n_eff)
                index = index + 1
                stations = stations[:index]
                stations.append({'ID':item['ID'],'T':T_out,'P':P_out})

            if item['TYPE'] == 'COMBUSTOR':
                P_in = stations[index]['P']
                T_in = stations[index]['T']
                T_out = item['TET']
                Q_in = cp_calc(T_out)*(T_out - T_in)*mass_flow
                fuel_flow = Q_in/LHV
                mass_flow = mass_flow + fuel_flow
                total_flow = total_flow + fuel_flow
                stations.append({'ID':item['ID'],'T':T_out,'P':P_out*(1-item['P_LOSS'])})
                index = index + 1

            if item['TYPE'] == 'POWER_TURBINE':
                T_in = stations[index]['T']
                P_in = stations[index]['P']
                cp_turb = cp_calc(T_in)
                M_exit = item['M_EXIT']
                y = gamma_calc(T_amb)

                P_out = P_amb*(1+(y-1)/2*M_exit**2)**(y/(y-1));
                T_out_is = T_in*(P_in/P_out)**((1-y)/y);
                T_out = T_in - (T_in-T_out_is)*item['EFF'];

                # subtract the residual work from net work
                W_net = (T_in-T_out)*cp_turb*mass_flow;
                for x in item['W_MATCH']:
                    W_net = W_net - works[x]

                stations.append({'ID':item['ID'],'T':T_out,'P':P_out})
                index = index +1
    # print report
    print ('SUMMARY:')
    #for item in stations:
    #    print ('\t %s' % item)
    print ("\tEngine class: %s" % engine_class)
    print ("\tTotal mass flow: %3.2f kg/s" % total_flow)
    print ("\tFuel flow: %3.2f kg/s" %(fuel_flow))
    if engine_class == 'TURBOSHAFT':
        print ("\tThermal efficiency: %3.2f%%" % (W_net*100/Q_in))
        print ("\tAvailable shaft power: %3.2f MW" % (W_net/1000000))
        print ("\tSFC is %3.3f kg/s/MW" % (fuel_flow/(W_net/1000000)))
    else:
        print ("\tThermal efficiency: %3.2f%%" % (sum(energies)*100/Q_in))
        print ("\tNet thrust: %3.2f kN" % (sum(thrusts)/1000))
        print ("\tSFC is %3.3f kg/s/kN" % (fuel_flow/(sum(thrusts)/1000)))

print('hello')
# plot_cycle_charts(t1,t2,t3,t4,p1,p2,p3,p4)
#compute_engine(ENGINE_1, OPTIONS)
compute_engine(ENGINE_6)
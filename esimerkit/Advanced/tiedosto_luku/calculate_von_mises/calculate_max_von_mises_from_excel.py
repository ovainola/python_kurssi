# -*- coding: utf-8 -*-
# http://openpyxl.readthedocs.org/en/2.3.3/usage.html
import openpyxl
import numpy as np

def von_mises_stress(eigen_vals):
    """Calculate von Mises stress
    
    https://en.wikipedia.org/wiki/Von_Mises_yield_criterion
    """
    term_1 = eigen_vals[0] - eigen_vals[1]
    term_2 = eigen_vals[1] - eigen_vals[2]
    term_3 = eigen_vals[2] - eigen_vals[0]
    return np.sqrt(0.5 * (term_1 ** 2 + term_2 ** 2 + term_3 ** 2))

def create_tensor_notation(stress_components):
    """Transform from voigt notation to tensor notation
    """
    stress_tensor = np.zeros((3,3))
    stress_tensor[0, 0] = stress_components[0]
    stress_tensor[0, 1] = stress_components[5]  
    stress_tensor[0, 2] = stress_components[4]  
    stress_tensor[1, 0] = stress_components[5]  
    stress_tensor[1, 1] = stress_components[1]  
    stress_tensor[1, 2] = stress_components[3] 
    stress_tensor[2, 0] = stress_components[4] 
    stress_tensor[2, 1] = stress_components[3] 
    stress_tensor[2, 2] = stress_components[2]
    return stress_tensor

def calculate_max_von_mises(stress_hist):
    """Calculate maximum von mises over time
    """
    steps, dim = stress_hist.shape
    max_stress = -1e15
    for each in np.arange(steps):
        tensor = create_tensor_notation(stress_hist[each])
        eigen_values, eigen_vectors = np.linalg.eig(tensor)
        v_stress = von_mises_stress(eigen_values)
        if v_stress > max_stress:
            max_stress = v_stress
    return max_stress

if __name__ == '__main__':
    wb = openpyxl.load_workbook('node_data.xlsx')
    sheet_1 = wb.get_sheet_by_name("Sheet1")
    print(sheet_1["A1"].value)
    
    rivien_maara = len(sheet_1.rows)
    nodes_stress_in_voigt = np.zeros((rivien_maara-1, 2, 6))
    node_ids = np.zeros(rivien_maara)
    
    base_numero = 65
    start_column = 2
    for row_idx, row_number in enumerate(np.arange(2, rivien_maara+1)):
        node_ids[row_idx] = sheet_1["A{0}".format(row_number)].value
        for column in np.arange(1, 13):
            stress_arvo = sheet_1["{0}{1}".format(chr(base_numero + column), row_number)].value
            step = 0 if column < 7 else 1
            stress_component = (column - 1) % 6
            nodes_stress_in_voigt[row_idx, step, stress_component] = stress_arvo
            
    von_mises_stresses = np.zeros(rivien_maara-1)
    for each in np.arange(rivien_maara-1):
        von_mises_stresses[each] = calculate_max_von_mises(nodes_stress_in_voigt[each])
    
    print("Maximum von Mises (envelope): {0:.3f} MPa".format(max(von_mises_stresses)))
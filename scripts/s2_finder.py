


import numpy as np
#import pylab as pl
import matplotlib.pyplot as pl
import matplotlib as mpl
import scipy
from scipy.signal import find_peaks
from scipy.signal import argrelmin
import time
def smooth(data,t_min,window):
    avg_array=np.zeros(len(data))
    #print(avg_array)
    m=20
    for i in range(t_min, t_min+window):
        min_ind=i-m
        max_ind=i+m
        if min_ind<0: min_ind=0
        if max_ind>len(data): max_ind = len(data)
        avg_array[i]=(np.mean(data[min_ind:max_ind]))
    return(avg_array)
#def maxima(data):
    #y = data
    #peaks = argrelextrema(y, np.greater)
   #return(peaks)
#def minima(data):
    #z = data
    #valleys = argrelextrema(z, np.less)
    #return(valleys)
def pulse_finder_area(data,t_min_search,t_max_search,window):
# Assumes data is already baseline-subtracted
    max_area=-1
    max_ind=-1
    for i_start in range(t_min_search,t_max_search):
        area=np.sum(data[i_start:i_start+window])
        if area>max_area:
            max_area=area
            max_ind=i_start
    return (max_ind, max_area)

def pulse_bounds(data,t_min,window,start_frac,end_frac):
    
# Assumes data is already baseline-subtracted
    start_pos=-1
    end_pos=-1
    peak_val=np.max(data[t_min:t_min+window])
    peak_pos=np.argmax(data[t_min:t_min+window])
    #start_frac: pulse starts at this fraction of peak height above baseline
    for i_start in range(t_min,t_min+window):
        if data[i_start]>max(peak_val*start_frac,4.5/chA_spe_size):
            start_pos=i_start
            break
    #end_frac: pulse ends at this fraction of peak height above baseline
    for i_start in range(t_min+window,t_min,-1):
        if data[i_start]>max(peak_val*end_frac,4.5/chA_spe_size):
            end_pos=i_start
            break
           
    return (start_pos, end_pos)
def merged_bounds(data, t_min, window, start_frac, end_frac):
    start_pos=-1
    end_pos=-1
    a = (np.diff(np.sign(np.diff(output))) > 0).nonzero()[0] + 1
    b = argrelmin(data)
    peak_v=np.max(data[t_min:t_min+window])
    print("b:", b)
    second = []
    print("a[0]:", a[0])
    for i in scipy.nditer(b):
        #if data[i]>0.2 and max(data[t_min:t_min+window]) < i : 
            #for i_start in range(t_min,t_min+window):
                #if data[i_start]>max(data[a[0]]*start_frac,4.5/chA_spe_size):
                    #start_pos=i_start
                    #break
        if data[i]>1:
            start_pos=i
            print("i:",i)
            break
 
    for j in a:
            
        if data[j]>0.2:
            second.append(j)
    for k in scipy.nditer(b):
        if max(a) > k:
            
            for z in second[1:]:       
       
    #end_frac: pulse ends at this fraction of peak height above baseline
                for i_start in range(t_min+window,t_min,-1):
                    if data[i_start]>max(data[z]*end_frac,4.5/chA_spe_size):
                        end_pos=i_start
                        break
        else:
            end_pos = b[0]
           
    return(start_pos, end_pos) 
# set plotting style
mpl.rcParams['font.size']=28
mpl.rcParams['legend.fontsize']='small'
mpl.rcParams['figure.autolayout']=True
mpl.rcParams['figure.figsize']=[16.0,12.0]

#channel_0=np.fromfile("wave0.dat", dtype="int16")
#channel_1=np.fromfile("wave1.dat", dtype="int16")
#channel_2=np.fromfile("wave2.dat", dtype="int16")
#channel_3=np.fromfile("wave3.dat", dtype="int16")

channel_0=np.fromfile("../../Desktop/crystallize_data/091319/A_3.2g_3.6c_50mV_Th232_frozen.dat", dtype="int16")
channel_1=np.fromfile("../../Desktop/crystallize_data/091319/B_3.2g_3.6c_50mV_Th232_frozen.dat", dtype="int16")
channel_2=np.fromfile("../../Desktop/crystallize_data/091319/C_3.2g_3.6c_50mV_Th232_frozen.dat", dtype="int16")
channel_3=np.fromfile("../../Desktop/crystallize_data/091319/D_3.2g_3.6c_50mV_Th232_frozen.dat", dtype="int16")

#channel_0=np.fromfile("../../Desktop/crystallize_data/t3-0805/A-thorium-4kv-t3.dat", dtype="int16")
#channel_1=np.fromfile("../../Desktop/crystallize_data/t3-0805/B-thorium-4kv-t3.dat", dtype="int16")
#channel_2=np.fromfile("../../Desktop/crystallize_data/t3-0805/C-thorium-4kv-t3.dat", dtype="int16")
#channel_3=np.fromfile("../../Desktop/crystallize_data/t3-0805/D-thorium-4kv-t3.dat", dtype="int16")

#channel_0=np.fromfile("A-thorium-3kv.dat", dtype="int16")
#channel_1=np.fromfile("B-thorium-3kv.dat", dtype="int16")
#channel_2=np.fromfile("C-thorium-3kv.dat", dtype="int16")
#channel_3=np.fromfile("D-thorium-3kv.dat", dtype="int16")

#channel_0=np.fromfile("A-thorium-2kv.dat", dtype="int16")
#channel_1=np.fromfile("B-thorium-2kv.dat", dtype="int16")
#channel_2=np.fromfile("C-thorium-2kv.dat", dtype="int16")
#channel_3=np.fromfile("D-thorium-2kv.dat", dtype="int16")

#channel_0=np.fromfile("A-thorium-1kv.dat", dtype="int16")
#channel_1=np.fromfile("B-thorium-1kv.dat", dtype="int16")
#channel_2=np.fromfile("C-thorium-1kv.dat", dtype="int16")
#channel_3=np.fromfile("D-thorium-1kv.dat", dtype="int16")



vscale=(2000.0/16384.0)
wsize=12500
chA_spe_size = 64.4
V=vscale*channel_0/chA_spe_size # ch A, calib size 644 
# Ensure we have an integer number of events
V=V[:int(len(V)/wsize)*wsize]
chB_spe_size = 50.5
V_1=vscale*channel_1/chB_spe_size
V_1=V_1[:int(len(V)/wsize)*wsize]
chC_spe_size = 33.9
V_2=vscale*channel_2/chC_spe_size
V_2=V_2[:int(len(V)/wsize)*wsize]
chD_spe_size = 30.6
V_3=vscale*channel_3/chD_spe_size
V_3=V_3[:int(len(V)/wsize)*wsize]
n_channels=5 # including sum
v_matrix = V.reshape(int(V.size/wsize),wsize)
v1_matrix = V_1.reshape(int(V.size/wsize),wsize)
v2_matrix = V_2.reshape(int(V.size/wsize),wsize)
v3_matrix = V_3.reshape(int(V.size/wsize),wsize)
v4_matrix = v_matrix+v1_matrix+v2_matrix+v3_matrix
v_matrix_all_ch=[v_matrix,v1_matrix,v2_matrix,v3_matrix,v4_matrix]
x=np.arange(0, wsize, 1)
tscale=(8.0/4096.0)
t=tscale*x
t_matrix=np.repeat(t[np.newaxis,:], V.size/wsize, 0)
# One entry per channel
max_ind_array=np.zeros((v_matrix.shape[0],n_channels) )
max_val_array=np.zeros((v_matrix.shape[0],n_channels) )
integral_array=np.zeros((v_matrix.shape[0],n_channels) )
s2_integral_array=np.zeros((v_matrix.shape[0],n_channels) )
s1_ch_array=np.zeros((v_matrix.shape[0],n_channels-1) )
s2_ch_array=np.zeros((v_matrix.shape[0],n_channels-1) )
# One entry per event
s2_area_array=np.zeros(v_matrix.shape[0])
s1_area_array=np.zeros(v_matrix.shape[0])
s2_width_array=np.zeros(v_matrix.shape[0])
s2_height_array=np.zeros(v_matrix.shape[0])
t_drift_array=np.zeros(v_matrix.shape[0])
s2_found_array=np.zeros(v_matrix.shape[0],dtype='bool')
s1_found_array=np.zeros(v_matrix.shape[0],dtype='bool')


# s2_area_array=[]
# s1_area_array=[]
# s2_width_array=[]
# t_drift_array=[]
# s2_found_array=[]
# s1_found_array=[]

inn=""
center = np.zeros(v_matrix.shape[0], dtype='bool')
print("Total events: ",v_matrix.shape[0])
for i in range(0, int(v_matrix.shape[0])):
    if i%100==0: print("Event #",i)
    t0=time.time()
    # for each channel
    for j in range(0, n_channels):
        #i = input("Window number between 1 and " + str((V.size/wsize)) + ": ")
        
        baseline=np.mean(v_matrix_all_ch[j][i,:500]) #avg ~1 us
        #print("baseline: ",baseline)
        
        win_min=int(18./tscale)
        win_max=int(21./tscale)
        integral=np.sum(v_matrix_all_ch[j][i,win_min:win_max]-baseline)
        integral_array[i,j]=integral
        # Threshold integral for trigger at 770: 1.9e5
		
		
        #print("Below is max index")
        max_ind=tscale*np.argmax(v_matrix_all_ch[j][i,:])
        max_ind_array[i,j]=max_ind
        #print(max_ind) 
        #print("Below is max value")
        max_val=np.max(v_matrix_all_ch[j][i,:])
        max_val_array[i,j]=max_val
        #print(max_val)
        
	# Look for events with S1 and S2 from summed channel
    s1_window = int(0.5/tscale)
    s2_window = int(1.5/tscale)
    s1_thresh = 400/chA_spe_size
    s1_range_thresh = 10/chA_spe_size
    s2_thresh = 1e3/chA_spe_size
    s1_max=s1_thresh
    s1_max_ind=-1
    s1_area=-1
    s1_height_range=-1
    s1_start_pos=-1
    s1_end_pos=-1
    s2_max=s2_thresh
    s2_max_ind=-1
    s2_area=-1
    #s2_start_pos=[]
    #s2_end_pos=[]
    s2_width=-1
    s2_height=-1
    t_drift=-1
    s1_found=False
    s2_found=False
    s1_ch_area=[-1]*(n_channels-1)
    s2_ch_area=[-1]*(n_channels-1)
    fiducial = False
 
    baseline_start = int(0./tscale)
    baseline_end = int(2./tscale)
    t0=time.time()
    sum_baseline=np.mean(v4_matrix[i,baseline_start:baseline_end]) #avg ~us, avoiding trigger
    baselines = [np.mean(ch_j[i,baseline_start:baseline_end] ) for ch_j in v_matrix_all_ch]
    print("baseline:", baselines)
    sum_data=v4_matrix[i,:]-sum_baseline
    ch_data=[ch_j[i,:]-baseline_j for (ch_j,baseline_j) in zip(v_matrix_all_ch,baselines)]
    t0a=time.time()
    #print("ch baseline calc time: ",t0a-t0)
      
    # Do a moving average (sum) of the waveform with different time windows for s1, s2
	# Look for where this value is maximized
	# Look for the s2 using a moving average (sum) of the waveform over a wide window
    t_min_search=int(10./tscale)
    t_max_search=int(22./tscale)
    t_offset=int(0.05/tscale)
    s2_max_ind, s2_max=pulse_finder_area(sum_data,t_min_search,t_max_search,s2_window)
    s2_found=s2_max>s2_thresh
    t1=time.time()
    #print("pulse finder time: ", t1-t0)
    
    output = smooth(sum_data,t_min_search,t_min_search+s2_window)
    #local_minima = minima(sum_data)
    t2=time.time()
    #local_maxima = maxima(sum_data)
    #print(len(t_matrix[i,:]))
    #print('local_max:', local_maxima)
    #print("smooth time: ", t2-t1)
    #print(output)
    if s2_found: # Found a pulse (maybe an s2)
        # print("s2 window time: ",s2_max_ind*tscale,"s2 area max: ",s2_max)
        start_frac=0.05 # pulse starts at this fraction of peak height above baseline
        end_frac=0.05 # pulse starts at this fraction of peak height above baseline
        s2_start_pos, s2_end_pos=pulse_bounds(sum_data,s2_max_ind-t_offset,s2_window,start_frac,end_frac)
        #s2_start_array, s2_end_array = merged_bounds(output,s2_max_ind-t_offset,s2_window,start_frac,end_frac)
        t3=time.time()
       
        #print('s2_start_array:', s2_start_array)
        #print('s2_end_array:', s2_end_array)
      
        #print("pulse bounds time: ", t3-t2)
        s2_area=np.sum(sum_data[s2_start_pos:s2_end_pos])
        s2_ch_area = [np.sum(ch[s2_start_pos:s2_end_pos]) for ch in ch_data]
       
      
        s2_width=(s2_end_pos-s2_start_pos)*tscale
        s2_height=np.max(sum_data[s2_start_pos:s2_end_pos])
        #s2_area_array.append(s2_area)
        #s2_width_array.append(s2_width)
        #s2_found_array.append(s2_found)
        #print("s2 start: ",s2_start_pos*tscale," s2 end: ",s2_end_pos*tscale)
        s2_mean = np.mean(s2_ch_area[:-1])
        fiducial = True
       
        for k in range(0,len(s2_ch_area)-1):
            print(s2_ch_area[k], s2_mean)
            if not (s2_ch_area[k] > 0.3*s2_mean and s2_ch_area[k] < 2*s2_mean):
                fiducial = False
                break
        print("fiducial? ", fiducial)        
        if fiducial:
            center[i] = True
        elif not fiducial:
            center[i] = False 	
        # Now look for a prior s1                                                   
        s1_max_ind, s1_max=pulse_finder_area(sum_data,t_min_search,s2_start_pos-s1_window-t_offset,s1_window)
        #print("s1 area: ",s1_max)
        if s1_max>s1_thresh:
            #print("s1 window time: ",s1_max_ind*tscale,"s1 area max: ",s1_max)    
            s1_start_pos, s1_end_pos = pulse_bounds(sum_data,s1_max_ind-t_offset,s1_window,0.1,0.1)
            if s1_start_pos > -1 and s1_end_pos > s1_start_pos:
               # print(s1_start_pos)
               # print(s1_end_pos)
                # Check that we didn't accidentally find noise (related to poor baseline subtraction)
                s1_height_range=np.max(sum_data[s1_start_pos:s1_end_pos])-np.min(sum_data[s1_start_pos:s1_end_pos]) 
                s1_found = s1_height_range>s1_range_thresh
                # print("s1 start: ",s1_start_pos*tscale," s1 end: ",s1_end_pos*tscale)
                if 0.60<t_drift<0.70:
                    print("s1_max_ind: ",s1_max_ind*tscale," s1_start_pos: ",s1_start_pos*tscale," tdrift: ",t_drift)
                    print("s1 range: ",s1_height_range)
                    print("baseline: ",sum_baseline)
                if not s1_found:
                    pass
                   # print("under range, s1 range: ",s1_height_range)
                else:    
                    t_drift=(s2_start_pos-s1_start_pos)*tscale
                    s1_area=np.sum(sum_data[s1_start_pos:s1_end_pos])
                    s1_ch_area = [np.sum(ch[s1_start_pos:s1_end_pos]) for ch in ch_data]
                    
                    #s1_found_array.append(s1_found)       
	            #s1_area_array.append(s1_area)
	            #t_drift_array.append(t_drift)
    t4=time.time()
    #print("remaining time: ",t4-t3)
	


    s2_area_array[i]=s2_area
    s2_width_array[i]=s2_width
    s2_height_array[i]=s2_height
    s1_area_array[i]=s1_area
    t_drift_array[i]=t_drift
    s1_found_array[i]=s1_found
    s2_found_array[i]=s2_found
    for j in range(n_channels-1):
        s1_ch_array[i,j] = s1_ch_area[j]
        s2_ch_array[i,j] = s2_ch_area[j]
	 
    # once per event
    #if s1_max_ind>-1 and not s1_height_range>s1_range_thresh:
    #if 1.5<t_drift:
    #if 1.08<t_drift<1.12:
    merge_start, merge_end = merged_bounds(output,s2_max_ind-t_offset,s2_window,start_frac,end_frac)
    s2_2 = merge_start > -1
    print("merge_start:", merge_start)
    print("merge_end:", merge_end)
    if True and not inn=='q' and fiducial:
    #if s1_found and s2_found:
        fig=pl.figure(1,figsize=(20, 20))
        pl.rc('xtick', labelsize=25)
        pl.rc('ytick', labelsize=25)
        
        ax=pl.subplot2grid((2,3),(0,0))
        pl.plot(t_matrix[i,:],v_matrix[i,:],'y')
        pl.xlim([0, 25])
        pl.ylim([0, 2500/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Phd/sample')
        pl.title("A,"+ str(i))
        triggertime_us = (t[-1]*0.2)
        pl.plot(np.array([1,1])*triggertime_us,np.array([0,16384]),'k--')

        if s2_found:
            ax.axvspan(s2_start_pos*tscale, s2_end_pos*tscale, alpha=0.5, color='blue')
        if s1_found:
            ax.axvspan(s1_start_pos*tscale, s1_end_pos*tscale, alpha=0.5, color='green')

        
        ax=pl.subplot2grid((2,3),(0,1))
        pl.plot(t_matrix[i,:],v1_matrix[i,:],'cyan')
        pl.xlim([0, 25])
        pl.ylim([0, 2500/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Phd/sample')
        pl.title("B,"+ str(i))
        triggertime_us = (t[-1]*0.2)
        pl.plot(np.array([1,1])*triggertime_us,np.array([0,16384]),'k--')
        
        if s2_found:
            ax.axvspan(s2_start_pos*tscale, s2_end_pos*tscale, alpha=0.5, color='blue')
        if s1_found:
            ax.axvspan(s1_start_pos*tscale, s1_end_pos*tscale, alpha=0.5, color='green')


        ax=pl.subplot2grid((2,3),(0,2))
        pl.plot(t_matrix[i,:],v2_matrix[i,:],'magenta')
        pl.xlim([0, 25])
        pl.ylim([0, 2500/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Phd/sample')
        pl.title("C,"+ str(i))
        triggertime_us = (t[-1]*0.2)
        pl.plot(np.array([1,1])*triggertime_us,np.array([0,16384]),'k--')

        if s2_found:
            ax.axvspan(s2_start_pos*tscale, s2_end_pos*tscale, alpha=0.5, color='blue')
        if s1_found:
            ax.axvspan(s1_start_pos*tscale, s1_end_pos*tscale, alpha=0.5, color='green')

        
        ax=pl.subplot2grid((2,3),(1,0))
        pl.plot(t_matrix[i,:],v3_matrix[i,:],'blue')
        pl.xlim([0, 25])
        pl.ylim([0, 2500/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Phd/sample')
        pl.title("D,"+ str(i))
        triggertime_us = (t[-1]*0.2)
        pl.plot(np.array([1,1])*triggertime_us,np.array([0,16384]),'k--')
        
        if s2_found:
            ax.axvspan(s2_start_pos*tscale, s2_end_pos*tscale, alpha=0.5, color='blue')
        if s1_found:
            ax.axvspan(s1_start_pos*tscale, s1_end_pos*tscale, alpha=0.5, color='green')
   

        #pl.figure()
        #pl.plot(t_matrix[i,:], smooth, 'blue')
        #pl.xlim([0,10])
        #pl.ylim([0,2500])

        #pl.xlabel('Time (us)')
        #pl.ylabel('Millivolts')
        #pl.title('average')
        #pl.show()






        pl.figure()
        pl.plot
        pl.plot(t_matrix[i,:],output,'blue')
       

        time_array=[]
        for o in t_matrix[i,:]:
            time_array.append(o)
   
          
        t = np.asarray(time_array)
        b = (np.diff(np.sign(np.diff(output))) > 0).nonzero()[0] + 1         # list of index locations of maxima
        c = (np.diff(np.sign(np.diff(output))) < 0).nonzero()[0] + 1         # list of index locations of minima
        for k in b:
            
            if output[k]>1:
                print('output[k]:', output[k])
                pl.plot(t[k], output[k], marker ='o', color='b')
                print("maxima:", k)
        for a in c:
            if output[a]>1:
                pl.plot(t[a],output[a],marker='o', color='r')
                print("minima:", a)            
        pl.xlim([0,25])
        pl.ylim([0,6000/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Millivolts')
        pl.title("SMOOTH")
        pl.show()


        ax=pl.subplot2grid((2,3),(1,1),colspan=2)
        pl.plot(t_matrix[i,:],v4_matrix[i,:],'blue')
        pl.xlim([0, 25])
        pl.ylim([0, 6000/chA_spe_size])
        pl.xlabel('Time (us)')
        pl.ylabel('Phd/sample')
        pl.title("Sum,"+ str(i))
        triggertime_us = (t[-1]*0.2)
        #pl.plot(np.array([1,1])*triggertime_us,np.array([0,16384]),'k--')
        if s2_found:
            ax.axvspan(s2_start_pos*tscale, s2_end_pos*tscale, alpha=0.5, color='blue')
        if s1_found:
            ax.axvspan(s1_start_pos*tscale, s1_end_pos*tscale, alpha=0.5, color='green')
        if s2_2:
            ax.axvspan(merge_start*tscale, merge_end*tscale, alpha=0.5, color='yellow')
        pl.draw()
        pl.show(block=0)
        inn = input("Press enter to continue, q to skip plotting")
        fig.clf()
s2_frac_array = s2_ch_array/s2_area_array.reshape(np.size(s2_area_array),1)
s1_frac_array = s1_ch_array/s1_area_array.reshape(np.size(s1_area_array),1)
print("s2_frac_Array sum:",np.sum(s2_frac_array, axis=1))
print("s1_frac_array sum:", np.sum(s1_frac_array, axis=1))
s2_frac_sum=(np.sum(s2_frac_array, axis=1))[s2_found_array*s1_found_array]
print("s2_frac_sum where not 1:",s2_frac_sum[np.where(s2_frac_sum < 0.99)[0]])
print("s2_found_array:", len(s2_found_array))
print("s1_found_array:", len(s1_found_array))
print("center:", len(center))
print("Events w/ S1+S2 fiducial: ",s2_area_array[s2_found_array*s1_found_array*center].size)
print("Events w/ S1+S2: ",s2_area_array[s2_found_array*s1_found_array].size)
print("S2 Area mean: ", np.mean(s2_area_array[s2_found_array*s1_found_array]))
print("S2 width mean: ", np.mean(s2_width_array[s2_found_array*s1_found_array]))
print("S2 height mean: ", np.mean(s2_height_array[s2_found_array*s1_found_array]))
print("Drift time mean: ", np.mean(t_drift_array[s2_found_array*s1_found_array]))
print("S1 Area mean: ", np.mean(s1_area_array[s2_found_array*s1_found_array]))
long_drift = t_drift_array > 0.7
pl.figure(figsize=(20, 20))
for j in range(0, n_channels):   
    pl.subplot(3,2,j+1)
    pl.hist(max_ind_array[:,j],bins=100)
    pl.yscale('log')
    pl.xlabel("Time of max value")
    pl.title('Ch '+str(j))
pl.figure(figsize=(20, 20))
for j in range(0, n_channels):    
    pl.subplot(3,2,j+1)  
    pl.hist(max_val_array[:,j],bins=100)
    pl.xlabel("Max value")
    pl.yscale('log')
    pl.title('Ch '+str(j))
pl.figure(figsize=(20, 20))
for j in range(0, n_channels):    
    pl.subplot(3,2,j+1)
    pl.hist(integral_array[:,j],bins=100,range=(-100,1500))
    pl.xlabel("Pulse integral")
    #pl.yscale('log')
    pl.title('Ch '+str(j))
pl.figure(figsize=(20, 20))
for j in range(0, n_channels-1):   
    pl.subplot(2,2,j+1)
    pl.hist(s1_ch_array[s2_found_array*s1_found_array][:,j],bins=100,range=(0,100))
    #pl.yscale('log')
    pl.xlabel("S1 area (phd)")
    pl.title('Ch '+str(j))
pl.figure(figsize=(20, 20))
for j in range(0, n_channels-1):   
    pl.subplot(2,2,j+1)
    pl.hist(s2_ch_array[s2_found_array*s1_found_array][:,j],bins=100,range=(0,4000))
    #pl.yscale('log')
    pl.xlabel("S2 area (phd)")
    pl.title('Ch '+str(j))


pl.figure(figsize=(20,20))
for j in range(0, n_channels-1):
    pl.subplot(2,2,j+1)
    pl.hist2d(t_drift_array[s2_found_array*s1_found_array*long_drift], s1_frac_array[s2_found_array*s1_found_array*long_drift][:,j], bins=100, range=[[0,6],[0,1]], norm=mpl.colors.LogNorm())
    pl.minorticks_on()
    if j == 0:
        pl.xlabel("drift time")
        pl.ylabel("S1_CH_A/S1")
    elif j == 1:
        pl.xlabel("drift time")
        pl.ylabel("S1_CH_B/S1")
    elif j == 2:
        pl.xlabel("drift time")
        pl.ylabel("S1_CH_C/S1")
    elif j == 3:
        pl.xlabel("drift time")
        pl.ylabel("S1_CH_D/S1")

pl.figure(figsize=(20,20))
for j in range(0, n_channels-1):
    pl.subplot(2,2,j+1)
    pl.hist2d(t_drift_array[s2_found_array*s1_found_array*long_drift], s2_frac_array[s2_found_array*s1_found_array*long_drift][:,j], bins=100,range=[[0,6],[0,1]], norm=mpl.colors.LogNorm())
    pl.minorticks_on()
    if j == 0:
        pl.xlabel("drift time")
        pl.ylabel("S2_CH_A/S2")
    elif j == 1:
        pl.xlabel("drift time")
        pl.ylabel("S2_CH_B/S2")
    elif j == 2:
        pl.xlabel("drift time")
        pl.ylabel("S2_CH_C/S2")
    elif j == 3:
        pl.xlabel("drift time")
        pl.ylabel("S2_CH_D/S2")

pl.figure()
pl.hist(s2_area_array[s2_found_array*s1_found_array*center],bins=100)
pl.axvline(x=np.mean(s2_area_array[s2_found_array*s1_found_array*center]),ls='--',color='r')
pl.xlabel("S2 area (phd)")

pl.figure()
pl.hist(s1_area_array[s2_found_array*s1_found_array*center],bins=200,range=(0,20000/chA_spe_size))#(t_drift_array>0.3)
pl.axvline(x=np.mean(s1_area_array[s2_found_array*s1_found_array]),ls='--',color='r')
pl.xlabel("S1 area (phd)")

pl.figure()
pl.hist(s2_width_array[s2_found_array*s1_found_array],bins=100)
pl.axvline(x=np.mean(s2_width_array[s2_found_array*s1_found_array]),ls='--',color='r')
pl.xlabel("S2 width (us)")

pl.figure()
pl.hist(s2_height_array[s2_found_array*s1_found_array],bins=100)
pl.axvline(x=np.mean(s2_height_array[s2_found_array*s1_found_array]),ls='--',color='r')
pl.xlabel("S2 height (mV)")   
pl.figure()
pl.hist(t_drift_array[s2_found_array*s1_found_array],bins=100)
pl.xlabel("drift time (us)")

t_drift_plot=t_drift_array[s2_found_array*s1_found_array]
s2_width_plot=s2_width_array[s2_found_array*s1_found_array]
s2_area_plot=s2_area_array[s2_found_array*s1_found_array]
pl.figure()
pl.scatter(t_drift_plot,s2_area_plot)
pl.xlabel("drift time (us)")
pl.ylabel("S2 area (phd)")

drift_bins=np.linspace(0,5,50)
drift_ind=np.digitize(t_drift_plot, bins=drift_bins)
s2_means=np.zeros(np.shape(drift_bins))
s2_std_err=np.ones(np.shape(drift_bins))*10000
for i_bin in range(len(drift_bins)):
    found_i_bin = np.where(drift_ind==i_bin) 
    s2_area_i_bin = s2_area_plot[found_i_bin]
    if len(s2_area_i_bin) < 1: continue
    s2_means[i_bin]=np.median(s2_area_i_bin)
    s2_std_err[i_bin]=np.std(s2_area_i_bin)/np.sqrt(len(s2_area_i_bin))
pl.errorbar(drift_bins, s2_means, yerr=s2_std_err, linewidth=3, elinewidth=3, capsize=5, capthick=4, color='red')


pl.figure()
pl.scatter(s2_area_plot,s2_width_plot)
pl.xlabel("S2 area (phd)")
pl.ylabel("S2 width (us)")

pl.show()
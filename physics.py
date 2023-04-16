import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
global G
G = 6.67e-11




def update_sim(frame, fig, params):
     
#----------------------------Parameters----------------------
    x = params["x"]
    y = params["y"]
    z = params["z"]
    v = params["v"]
    mask = params["mask"]

    n_particles, dt = params["n_particles"], params["dt"]
    mass = params["mass"]

    if frame%100 == 0: print("frame: ",frame) 
#-----------------------------update---------------------------

#compute difference of particle positions (avoiding fot the particle withs itself)
    diffx = torch.masked_select(torch.stack([(x-xi) for xi in x]), mask).reshape(n_particles,-1)
    diffy = torch.masked_select(torch.stack([(y-yi) for yi in y]), mask).reshape(n_particles,-1)
    diffz = torch.masked_select(torch.stack([(z-zi) for zi in z]), mask).reshape(n_particles,-1)

    distance = torch.sqrt(diffx**2 + diffy**2 + diffz**2) #compunting distance matrix

    #acceleration given by force/mass
    ax = torch.sum((G*mass.repeat(n_particles).reshape(n_particles, -1)[mask]).reshape(n_particles, -1)* diffx/(distance**3 + 1e-4) , dim=1)
    ay = torch.sum((G*mass.repeat(n_particles).reshape(n_particles, -1)[mask]).reshape(n_particles, -1)* diffy/(distance**3 + 1e-4) , dim=1)
    az = torch.sum((G*mass.repeat(n_particles).reshape(n_particles, -1)[mask]).reshape(n_particles, -1)* diffz/(distance**3 + 1e-4) , dim=1)

    #updating velocity and position
    v[0] += dt*ax
    x += v[0]*dt + 0.5*ax*dt**2

    v[1] += dt*ay
    y += v[1]*dt + 0.5*ay*dt**2

    v[2] += dt*az
    z += v[2] *dt + 0.5*az*dt**2

    # Update the Plotly figure
    fig.data[0].x = x
    fig.data[0].y = y
    fig.data[0].z = z

    params["x"], params["y"], params["z"] = x,y,z
 
    return fig.data, fig, params
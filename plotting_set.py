import plotly.graph_objects as go


def set_figure(x,y,z, size, colors):

        fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=size,
            color=colors,
            colorscale='Viridis',
            opacity=0.8,
        ),
        # Add the uirevision parameter to enable scene rotation
        uirevision=True
        )])
        
        return fig

def animate_setting(fig, space_size):
    fig.update_layout(scene=dict(
                    xaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    yaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    zaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    ),
                  updatemenus=[dict(type='buttons',
                                    showactive=False,
                                    buttons=[dict(label='Play',
                                                  method='animate',
                                                  args=[None,
                                                        dict(frame=dict(duration=50),
                                                             fromcurrent=True,
                                                             transition=dict(duration=0)
                                                             ),
                                                        dict(frame=dict(duration=0, redraw=False),
                                                             mode='immediate',
                                                             transition=dict(duration=0)
                                                             )
                                                        ]
                                                  ),
                                             dict(label='Stop',
                                                  method='animate',
                                                  args=[[None],
                                                        dict(frame=dict(duration=0, redraw=False),
                                                             mode='immediate',
                                                             transition=dict(duration=0)
                                                             )
                                                        ]
                                                  ),
                                            dict(label="Restart", 
                                                 method="animate", 
                                                 args=[None,
                                                       dict(frame=dict(duration= 50,
                                                                       fromcurrent= False, 
                                                                       redraw= True),
                                                            mode='immediate', 
                                                             )
                                                        ]
                                                  )
                                             ]
                                    )
                             ],
                  paper_bgcolor="black",
                  scene_bgcolor="black",
                  scene_aspectmode='data',
                  title='Particle Simulation',
                  showlegend=False,
                  width=1000,
                  height=800,
                  
                  )
    return fig

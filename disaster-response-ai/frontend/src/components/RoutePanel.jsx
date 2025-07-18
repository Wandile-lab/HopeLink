import React from 'react';
import { Card, CardContent, Typography, List, ListItem, ListItemIcon, ListItemText, Divider, Chip, Box } from '@mui/material';
import { DirectionsWalk, DirectionsCar, Warning, AccessTime } from '@mui/icons-material';

const RoutePanel = ({ routes }) => {
  return (
    <Card sx={{ height: '100%' }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Safe Route Suggestions
        </Typography>
        
        <List>
          {routes.map((route, index) => (
            <React.Fragment key={index}>
              <ListItem>
                <ListItemIcon>
                  {route.type === 'walking' ? <DirectionsWalk /> : <DirectionsCar />}
                </ListItemIcon>
                <ListItemText
                  primary={`${route.distance} km - ${route.duration}`}
                  secondary={route.summary}
                />
                <Box sx={{ display: 'flex', alignItems: 'center' }}>
                  <AccessTime fontSize="small" sx={{ mr: 1 }} />
                  <Typography variant="body2">{route.time}</Typography>
                </Box>
              </ListItem>
              
              {route.warnings.length > 0 && (
                <Box sx={{ pl: 9, pr: 2, mb: 2 }}>
                  {route.warnings.map((warning, i) => (
                    <Chip
                      key={i}
                      icon={<Warning />}
                      label={warning}
                      color="warning"
                      size="small"
                      sx={{ mr: 1, mb: 1 }}
                    />
                  ))}
                </Box>
              )}
              
              {index < routes.length - 1 && <Divider />}
            </React.Fragment>
          ))}
        </List>
      </CardContent>
    </Card>
  );
};

export default RoutePanel;
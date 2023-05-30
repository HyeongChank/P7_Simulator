import React, { useState } from 'react';
import { Canvas, useThree } from '@react-three/fiber';
import { useHover } from '@react-three/drei';

// Function for creating a single block
const Block = ({ position, dimensions, color }) => {
  const [hovered, events] = useHover();

  return (
    <mesh position={position} {...events}>
      {hovered && (
        <>
          <boxGeometry args={dimensions} />
          <meshBasicMaterial color={color} />
        </>
      )}
    </mesh>
  );
};
export default Block;
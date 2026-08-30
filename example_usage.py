from client import JointEmbeddingPredictiveWorldRepresentationClient

def main():
    client = JointEmbeddingPredictiveWorldRepresentationClient()
    res = client.predict_future_latent_world_state(128, 16)
    print('JEPA World Representation: ' + res['jepa_prediction_id'] + ' (Dim: ' + str(res['feature_space_dimension']) + ')')
    print('Pixel Reconstruction Bypassed: ' + str(res['pixel_reconstruction_bypassed']) + ' | Loss: ' + str(res['semantic_representation_loss']))
    print('Physical Consistency: ' + str(res['physical_world_dynamics_consistency_pct']) + '%')
    print('Latent Vectors: ' + res['latent_trajectory_vector_url'])

if __name__ == '__main__':
    main()
